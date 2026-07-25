## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/18

**Issue title:** Add end-to-end ingestion test with a sample resume fixture

**Tier:** [ ] Tier 1  [x] Tier 2  [ ] Tier 3

**Problem summary:**
The pipeline that ingests a resume — from file upload through parsing and into embedding storage — currently only has unit tests for individual parser components in isolation. There's no test verifying the full chain works together end-to-end. This issue asks for an integration test in `tests/integration/test_ingestion_pipeline.py` that uses existing sample resume fixtures in `tests/fixtures/sample_resumes/` to confirm a resume can be uploaded, parsed, embedded, and stored correctly in one continuous flow.

**Branch name:** test/18-e2e-ingestion-pipeline

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [x] Issue added to cohort ledger

## Week 8 — Reproduction & solution planning

**Reproduction commit link:** https://github.com/Sniggy26/pathreview/commit/c9cc479

**Reproduction summary:**
Confirmed via a direct Python script that `IngestionPipeline.ingest_resume()` already works end-to-end (parse → chunk → embed → store) when called directly, producing 1 chunk and storing it in a real ChromaDB collection. Also discovered the pipeline is never actually called from the API's resume upload endpoint, and that its dedupe-check and DB-recording methods are unfinished placeholders.

**PLAN.md link:** https://github.com/Sniggy26/pathreview/blob/test/18-e2e-ingestion-pipeline/PLAN.md

**Walkthrough video (recommended):** [not recorded this week]

**Blockers or open questions:**
Need to decide whether to build a proper test DB session fixture or use a lightweight fake for the `db_session` argument, since no Postgres-backed test fixture currently exists in `tests/conftest.py`. Also unsure whether the skip/dedupe test should assert current (buggy) behavior or flag it as a known gap without asserting on it.