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

---

### Check-in 2 (end of week)

**PR link:** https://github.com/ascherj/pathreview/pull/588

**Branch:** test/18-e2e-ingestion-pipeline

**What you built:**
An end-to-end integration test (`tests/integration/test_ingestion_pipeline.py`) covering the full resume ingestion chain — parse → chunk → embed → store — by calling `IngestionPipeline.ingest_resume()` directly against a real in-memory ChromaDB collection and a `MockEmbeddingProvider`. Along the way I found and documented two real cross-component bugs (an empty-metadata-list crash triggered by indented resume text, and a broken dedupe check) that unit tests alone hadn't caught.

**Tests added or updated:**
Added `tests/integration/test_ingestion_pipeline.py` with 3 tests: `test_ingest_resume_end_to_end` (happy path, asserts real storage via `collection.count()`), `test_ingest_resume_no_experience_section` (edge case with no Experience section), and `test_ingest_resume_duplicate_content_does_not_dedupe_today` (documents current dedupe behavior). Also added a fixture file at `tests/fixtures/sample_resumes/sample_resume.md`.

**Self-review confirmation:** [x] make check passes  [x] make test-unit passes
(Both pass in the sense defined by the assignment: no new failures introduced. `make test-unit` shows the same pre-existing 53 failures/375 passing before and after this PR. `make check`'s mypy step cannot complete on any file in the repo, including files untouched by this PR, due to a pre-existing `python_version`/numpy stub mismatch — documented in the PR and commit message. `ruff` and `black` both pass cleanly on my new file.)

**Draft PR feedback received from:** none