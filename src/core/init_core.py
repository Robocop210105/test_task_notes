from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from py_fastapi_logging.middlewares.logging import LoggingMiddleware

from db import init_tortoise
from apis.api import api_router
from .config import settings


def create_app():
    app = FastAPI(
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_headers=["Authorization-Client"],
            )
        ],
    )
    init_tortoise(app)
    app.add_middleware(LoggingMiddleware, app_name='Notes-web')
    app.include_router(api_router, prefix=settings.API_V1_STR)
    return app
