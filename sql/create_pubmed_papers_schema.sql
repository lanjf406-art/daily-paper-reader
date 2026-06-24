-- ============================================================
-- Create a PubMed-only paper table in the same Supabase project.
-- ============================================================

create extension if not exists vector;

create table if not exists public.pubmed_papers (
  id text primary key,
  source text not null default 'pubmed',
  source_paper_id text,
  pmid text,
  pmcid text,
  doi text,
  journal text,
  title text not null,
  abstract text,
  authors jsonb not null default '[]'::jsonb,
  primary_category text,
  categories jsonb not null default '[]'::jsonb,
  published timestamptz,
  link text,
  pdf_url text,
  embedding vector(384),
  embedding_model text,
  embedding_dim int,
  embedding_updated_at timestamptz,
  updated_at timestamptz not null default now()
);

create unique index if not exists pubmed_papers_pmid_idx
  on public.pubmed_papers (pmid)
  where pmid is not null and pmid <> '';

create index if not exists pubmed_papers_source_published_idx
  on public.pubmed_papers (source, published desc);

create index if not exists pubmed_papers_published_idx
  on public.pubmed_papers (published desc);

create index if not exists pubmed_papers_title_abstract_fts_idx
  on public.pubmed_papers
  using gin (to_tsvector('english', coalesce(title, '') || ' ' || coalesce(abstract, '')));
