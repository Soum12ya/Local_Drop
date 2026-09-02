CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Initial schema is represented by SQLAlchemy models in apps/api/app/models.py.
-- Production migrations should be generated and committed with Alembic.

CREATE INDEX IF NOT EXISTS idx_sellers_location
ON sellers USING GIST (location);
