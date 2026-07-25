"""
Integration test for the resume ingestion pipeline.

Reproduction (Week 8): confirmed no existing test exercises the full
upload -> parse -> chunk -> embed -> store chain. Manually verified via
python shell that IngestionPipeline.ingest_resume() works end-to-end
when called directly: parses resume text, produces 1 chunk, generates a
mock embedding, and stores it in a real ChromaDB collection
(collection.count() == 1 after ingestion).

Also confirmed during reproduction:
- IngestionPipeline is never called from api/routes/profiles.py; the
  upload endpoint parses resumes independently via raw PyPDF2 and never
  invokes the pipeline. There is no code path connecting HTTP upload to
  ingestion today.
- IngestionPipeline._check_skip() has a placeholder query
  (db_session.query("IngestedSource")) that will fail against a real
  SQLAlchemy session; it's wrapped in try/except so failures are logged
  and swallowed rather than raised.
- IngestionPipeline._record_ingested_source() only logs; it does not
  persist anything to Postgres despite its docstring.

This test will be built out in Week 9 to call IngestionPipeline directly
(bypassing the disconnected HTTP endpoint) using fixtures to be added at
tests/fixtures/sample_resumes/ (directory does not exist yet).
"""
