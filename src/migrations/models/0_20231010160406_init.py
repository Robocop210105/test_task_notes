from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "boardmodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "board_name" VARCHAR(100) NOT NULL,
    "time_create" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "time_change" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "notemodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "text_note" TEXT NOT NULL,
    "time_create" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "time_change" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "board_id_id" INT NOT NULL REFERENCES "boardmodel" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
