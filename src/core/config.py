import os

from pydantic_settings import BaseSettings

ENV = os.getenv("ENV_NAME") or "local"


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 5000
    API_V1_STR: str = ""
    DATABASE_URL: str = "postgres://{}:{}@{}/{}".format(
        os.getenv("POSTGRES_USER"),
        os.getenv("POSTGRES_PASSWORD"),
        os.getenv("POSTGRES_HOST"),
        os.getenv("POSTGRES_DB"),
    )
    APPS_MODELS: list = [
        "aerich.models",
        "models.notes_models",
        "models.boards_models",
    ]


settings = Settings()
