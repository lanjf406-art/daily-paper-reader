import importlib.util
import pathlib
import sys
import unittest


def _load_module(module_name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


class FetchPubMedTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = pathlib.Path(__file__).resolve().parents[1]
        src_dir = root / "src"
        if str(src_dir) not in sys.path:
            sys.path.insert(0, str(src_dir))
        cls.mod = _load_module("fetch_pubmed_mod", src_dir / "maintain" / "fetchers" / "fetch_pubmed.py")

    def test_build_pubmed_paper_id_requires_pmid(self):
        self.assertEqual(self.mod.build_pubmed_paper_id(" 123456 "), "pubmed-123456")
        self.assertEqual(self.mod.build_pubmed_paper_id(""), "")

    def test_parse_pubmed_xml_normalizes_verified_pubmed_record(self):
        xml = """<?xml version="1.0"?>
        <PubmedArticleSet>
          <PubmedArticle>
            <MedlineCitation>
              <PMID>123456</PMID>
              <Article>
                <ArticleTitle>Neoadjuvant immunotherapy in esophageal squamous cell carcinoma</ArticleTitle>
                <Abstract>
                  <AbstractText>Background text.</AbstractText>
                  <AbstractText Label="Results">Result text.</AbstractText>
                </Abstract>
                <Journal>
                  <Title>Journal of Clinical Oncology</Title>
                  <JournalIssue>
                    <PubDate>
                      <Year>2026</Year>
                      <Month>Jun</Month>
                      <Day>02</Day>
                    </PubDate>
                  </JournalIssue>
                </Journal>
                <AuthorList>
                  <Author><LastName>Wang</LastName><ForeName>Li</ForeName></Author>
                  <Author><CollectiveName>ESCC Study Group</CollectiveName></Author>
                </AuthorList>
                <ELocationID EIdType="doi">10.1200/test.doi</ELocationID>
              </Article>
            </MedlineCitation>
            <PubmedData>
              <ArticleIdList>
                <ArticleId IdType="pubmed">123456</ArticleId>
                <ArticleId IdType="pmc">PMC123456</ArticleId>
              </ArticleIdList>
            </PubmedData>
          </PubmedArticle>
        </PubmedArticleSet>
        """
        records = self.mod.parse_pubmed_xml(xml)
        self.assertEqual(len(records), 1)
        paper = records[0]
        self.assertEqual(paper["id"], "pubmed-123456")
        self.assertEqual(paper["source"], "pubmed")
        self.assertEqual(paper["source_paper_id"], "123456")
        self.assertEqual(paper["pmid"], "123456")
        self.assertEqual(paper["pmcid"], "PMC123456")
        self.assertEqual(paper["doi"], "10.1200/test.doi")
        self.assertEqual(paper["published"], "2026-06-02T00:00:00+00:00")
        self.assertIn("pubmed.ncbi.nlm.nih.gov/123456", paper["link"])
        self.assertIn("Background text.", paper["abstract"])
        self.assertEqual(paper["authors"], ["Li Wang", "ESCC Study Group"])

    def test_parse_pubmed_xml_drops_records_without_pmid(self):
        xml = """<PubmedArticleSet><PubmedArticle><MedlineCitation><Article><ArticleTitle>No PMID</ArticleTitle></Article></MedlineCitation></PubmedArticle></PubmedArticleSet>"""
        self.assertEqual(self.mod.parse_pubmed_xml(xml), [])


if __name__ == "__main__":
    unittest.main()
