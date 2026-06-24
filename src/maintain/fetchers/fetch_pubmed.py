#!/usr/bin/env python

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

try:
    from source_config import load_config_with_source_migration
except Exception:  # pragma: no cover
    from src.source_config import load_config_with_source_migration


SCRIPT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
CONFIG_FILE = os.path.join(ROOT_DIR, "config.yaml")
CRAWL_STATE_FILE = os.path.join(ROOT_DIR, "archive", "pubmed_crawl_state.json")
SEEN_IDS_FILE = os.path.join(ROOT_DIR, "archive", "pubmed_seen.json")
EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
DEFAULT_TOOL = "daily-paper-reader"
DEFAULT_QUERY = "cancer[Title/Abstract]"
MONTHS = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "sept": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


def log(message: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {message}", flush=True)


def group_start(title: str) -> None:
    print(f"::group::{title}", flush=True)


def group_end() -> None:
    print("::endgroup::", flush=True)


def _norm(value: Any) -> str:
    return str(value or "").strip()


def _text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return re.sub(r"\s+", " ", "".join(element.itertext())).strip()


def load_config() -> dict:
    try:
        return load_config_with_source_migration(CONFIG_FILE, write_back=False)
    except Exception as exc:
        log(f"[WARN] read config.yaml failed: {exc}")
        return {}


def resolve_pubmed_query(cli_query: str = "") -> str:
    direct = _norm(cli_query) or _norm(os.getenv("DPR_PUBMED_QUERY"))
    if direct:
        return direct
    cfg = load_config()
    setting = cfg.get("pubmed_setting") if isinstance(cfg, dict) else {}
    if isinstance(setting, dict):
        query = _norm(setting.get("query"))
        if query:
            return query
    return DEFAULT_QUERY


def resolve_days_window(default_days: int) -> int:
    cfg = load_config()
    setting = cfg.get("pubmed_setting") if isinstance(cfg, dict) else {}
    if isinstance(setting, dict):
        try:
            return max(int(setting.get("days_window") or default_days), 1)
        except Exception:
            return max(default_days, 1)
    return max(default_days, 1)


def build_pubmed_paper_id(pmid: Any) -> str:
    text = _norm(pmid)
    if not text:
        return ""
    return f"pubmed-{text}"


def _article_id(article: ET.Element, id_type: str) -> str:
    for node in article.findall(".//PubmedData/ArticleIdList/ArticleId"):
        if _norm(node.attrib.get("IdType")).lower() == id_type.lower():
            return _text(node)
    return ""


def _doi(article: ET.Element) -> str:
    for node in article.findall(".//Article/ELocationID"):
        if _norm(node.attrib.get("EIdType")).lower() == "doi":
            doi = _text(node)
            if doi:
                return doi
    return _article_id(article, "doi")


def _pmid(article: ET.Element) -> str:
    pmid = _text(article.find(".//MedlineCitation/PMID"))
    return pmid or _article_id(article, "pubmed")


def _parse_month(value: str) -> int:
    text = _norm(value).lower()
    if not text:
        return 1
    if text.isdigit():
        return min(max(int(text), 1), 12)
    return MONTHS.get(text[:4], MONTHS.get(text[:3], 1))


def _safe_date_iso(year: int, month: int = 1, day: int = 1) -> str:
    try:
        dt = datetime(year, month, day, tzinfo=timezone.utc)
    except Exception:
        dt = datetime(year, 1, 1, tzinfo=timezone.utc)
    return dt.isoformat()


def _date_from_pubdate(pubdate: ET.Element | None) -> str:
    if pubdate is None:
        return ""
    year_text = _text(pubdate.find("Year"))
    if not year_text:
        medline_date = _text(pubdate.find("MedlineDate"))
        matched = re.search(r"\b(19|20)\d{2}\b", medline_date)
        year_text = matched.group(0) if matched else ""
    if not year_text:
        return ""
    month = _parse_month(_text(pubdate.find("Month")))
    try:
        day = int(_text(pubdate.find("Day")) or "1")
    except Exception:
        day = 1
    return _safe_date_iso(int(year_text), month, day)


def _published(article: ET.Element) -> str | None:
    article_date = article.find(".//Article/ArticleDate")
    if article_date is not None:
        date_iso = _date_from_pubdate(article_date)
        if date_iso:
            return date_iso
    date_iso = _date_from_pubdate(article.find(".//Article/Journal/JournalIssue/PubDate"))
    return date_iso or None


def _abstract(article: ET.Element) -> str:
    parts: List[str] = []
    for node in article.findall(".//Article/Abstract/AbstractText"):
        text = _text(node)
        if not text:
            continue
        label = _norm(node.attrib.get("Label"))
        parts.append(f"{label}: {text}" if label else text)
    return "\n".join(parts)


def _authors(article: ET.Element) -> List[str]:
    out: List[str] = []
    seen = set()
    for node in article.findall(".//Article/AuthorList/Author"):
        collective = _text(node.find("CollectiveName"))
        if collective:
            name = collective
        else:
            fore = _text(node.find("ForeName"))
            last = _text(node.find("LastName"))
            name = " ".join(x for x in (fore, last) if x)
        if not name or name in seen:
            continue
        seen.add(name)
        out.append(name)
    return out


def parse_pubmed_xml(xml_text: str) -> List[Dict[str, Any]]:
    root = ET.fromstring(xml_text or "<PubmedArticleSet />")
    out: List[Dict[str, Any]] = []
    for article in root.findall(".//PubmedArticle"):
        pmid = _pmid(article)
        paper_id = build_pubmed_paper_id(pmid)
        if not paper_id:
            continue
        title = _text(article.find(".//Article/ArticleTitle"))
        journal = _text(article.find(".//Article/Journal/Title"))
        doi = _doi(article)
        pmcid = _article_id(article, "pmc")
        link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        pdf_url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/pdf/" if pmcid else ""
        row = {
            "id": paper_id,
            "source": "pubmed",
            "source_paper_id": pmid,
            "pmid": pmid,
            "pmcid": pmcid,
            "doi": doi,
            "title": title,
            "abstract": _abstract(article),
            "authors": _authors(article),
            "primary_category": journal or "PubMed",
            "categories": [journal] if journal else ["PubMed"],
            "published": _published(article),
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "link": link,
            "pdf_url": pdf_url,
            "abs_url": link,
            "journal": journal,
        }
        out.append(row)
    return out


def load_seen_state() -> tuple[set[str], datetime | None]:
    if not os.path.exists(SEEN_IDS_FILE):
        return set(), None
    try:
        with open(SEEN_IDS_FILE, "r", encoding="utf-8") as f:
            payload = json.load(f) or {}
    except Exception:
        return set(), None
    ids = payload.get("ids") if isinstance(payload, dict) else []
    seen_ids = {str(item).strip() for item in (ids if isinstance(ids, list) else []) if str(item).strip()}
    latest = None
    raw_latest = _norm(payload.get("latest_published_at") if isinstance(payload, dict) else "")
    if raw_latest:
        try:
            latest = datetime.fromisoformat(raw_latest.replace("Z", "+00:00"))
            if latest.tzinfo is None:
                latest = latest.replace(tzinfo=timezone.utc)
            latest = latest.astimezone(timezone.utc)
        except Exception:
            latest = None
    return seen_ids, latest


def save_seen_state(seen_ids: set[str], latest_published_at: datetime | None) -> None:
    os.makedirs(os.path.dirname(SEEN_IDS_FILE), exist_ok=True)
    payload = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "latest_published_at": latest_published_at.astimezone(timezone.utc).isoformat()
        if latest_published_at
        else "",
        "ids": sorted(seen_ids),
    }
    with open(SEEN_IDS_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def save_last_crawl_at(at_time: datetime) -> None:
    os.makedirs(os.path.dirname(CRAWL_STATE_FILE), exist_ok=True)
    with open(CRAWL_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump({"last_crawl_at": at_time.astimezone(timezone.utc).isoformat()}, f, ensure_ascii=False, indent=2)


def _published_dt(row: Dict[str, Any]) -> datetime | None:
    raw = _norm(row.get("published"))
    if not raw:
        return None
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except Exception:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def fetch_pubmed_ids(
    *,
    query: str,
    days: int,
    retmax: int,
    email: str = "",
    tool: str = DEFAULT_TOOL,
    timeout: int = 60,
) -> List[str]:
    import requests

    params: Dict[str, Any] = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max(int(retmax or 1), 1),
        "sort": "pub_date",
        "datetype": "edat",
        "reldate": max(int(days or 1), 1),
        "tool": tool,
    }
    if email:
        params["email"] = email
    resp = requests.get(f"{EUTILS_BASE}/esearch.fcgi", params=params, timeout=timeout)
    resp.raise_for_status()
    data = resp.json() or {}
    ids = ((data.get("esearchresult") or {}).get("idlist") or [])
    return [_norm(item) for item in ids if _norm(item)]


def fetch_pubmed_records(
    pmids: List[str],
    *,
    email: str = "",
    tool: str = DEFAULT_TOOL,
    timeout: int = 60,
    batch_size: int = 200,
) -> List[Dict[str, Any]]:
    import requests

    out: List[Dict[str, Any]] = []
    safe_ids = [_norm(item) for item in pmids if _norm(item)]
    for idx in range(0, len(safe_ids), max(int(batch_size or 1), 1)):
        chunk = safe_ids[idx : idx + max(int(batch_size or 1), 1)]
        params: Dict[str, Any] = {
            "db": "pubmed",
            "id": ",".join(chunk),
            "retmode": "xml",
            "tool": tool,
        }
        if email:
            params["email"] = email
        resp = requests.get(f"{EUTILS_BASE}/efetch.fcgi", params=params, timeout=timeout)
        resp.raise_for_status()
        out.extend(parse_pubmed_xml(resp.text))
        time.sleep(0.34)
    return out


def fetch_pubmed_metadata(
    *,
    query: str = "",
    days: int | None = None,
    retmax: int = 200,
    output_file: str | None = None,
    ignore_seen: bool = False,
    email: str = "",
) -> None:
    end_date = datetime.now(timezone.utc)
    safe_days = max(int(days or resolve_days_window(30)), 1)
    safe_query = resolve_pubmed_query(query)
    seen_ids, latest_published_at = (set(), None) if ignore_seen else load_seen_state()

    group_start("Step 1 - fetch PubMed")
    log(f"[PubMed Ingest] query={safe_query}")
    log(f"[PubMed Ingest] reldate={safe_days}, retmax={retmax}")
    pmids = fetch_pubmed_ids(
        query=safe_query,
        days=safe_days,
        retmax=max(int(retmax or 1), 1),
        email=email or _norm(os.getenv("NCBI_EMAIL")),
    )
    rows = fetch_pubmed_records(pmids, email=email or _norm(os.getenv("NCBI_EMAIL")))
    unique: Dict[str, Dict[str, Any]] = {}
    max_published_new = latest_published_at
    for row in rows:
        pid = _norm(row.get("id"))
        if not pid or pid in seen_ids:
            continue
        unique[pid] = row
        seen_ids.add(pid)
        dt = _published_dt(row)
        if dt and (max_published_new is None or dt > max_published_new):
            max_published_new = dt

    log(f"[PubMed Ingest] fetched_pmids={len(pmids)}, valid_new_records={len(unique)}")
    if not output_file:
        run_token = _norm(os.getenv("DPR_RUN_DATE")) or end_date.strftime("%Y%m%d")
        output_file = os.path.join(ROOT_DIR, "archive", run_token, "raw", f"pubmed_papers_{run_token}.json")
    os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else ".", exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(list(unique.values()), f, ensure_ascii=False, indent=2)
    log(f"File saved to: {output_file}")

    save_seen_state(seen_ids, max_published_new)
    save_last_crawl_at(end_date)
    group_end()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch PubMed metadata through NCBI E-utilities.")
    parser.add_argument("--query", type=str, default="", help="PubMed query. Defaults to pubmed_setting.query or DPR_PUBMED_QUERY.")
    parser.add_argument("--days", type=int, default=None, help="Entrez date reldate window.")
    parser.add_argument("--retmax", type=int, default=200, help="Maximum PMIDs returned by ESearch.")
    parser.add_argument("--output", type=str, default=None, help="Output JSON path.")
    parser.add_argument("--ignore-seen", action="store_true", help="Ignore archive/pubmed_seen.json state.")
    parser.add_argument("--email", type=str, default="", help="NCBI contact email.")
    args = parser.parse_args()
    fetch_pubmed_metadata(
        query=args.query,
        days=args.days,
        retmax=args.retmax,
        output_file=args.output,
        ignore_seen=bool(args.ignore_seen),
        email=args.email,
    )
