## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/18

**Issue title:** Add end-to-end ingestion test with a sample resume fixture

**Tier:** [ ] Tier 1  [x] Tier 2  [ ] Tier 3

**Problem summary:**
The pipeline that ingests a resume — from file upload through parsing and into embedding storage — currently only has unit tests for individual parser components in isolation. There's no test verifying the full chain works together end-to-end. This issue asks for an integration test in `tests/integration/test_ingestion_pipeline.py` that uses existing sample resume fixtures in `tests/fixtures/sample_resumes/` to confirm a resume can be uploaded, parsed, embedded, and stored correctly in one continuous flow.

**Branch name:** test/18-e2e-ingestion-pipeline

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [x] Issue added to cohort ledger