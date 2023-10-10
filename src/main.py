import uvicorn
from core.config import settings
from core.init_core import create_app
from tortoise import Tortoise

Tortoise.init_models(settings.APPS_MODELS, "models")
app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host=settings.host, port=settings.port)
