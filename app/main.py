from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from tortoise import Tortoise, generate_config
from tortoise.contrib.fastapi import RegisterTortoise

from app.logger import service_logger
from app.env_validator import get_settings
from app.containers import AppContainers

from app.hello.endpoints import router as auth_router

logger = service_logger("bootstrapper")
settings = get_settings()


def bootstrap() -> FastAPI:
    @asynccontextmanager
    async def lifespan(application: FastAPI) -> AsyncGenerator[None, None]:
        logger.info("Starting application")
        config = generate_config(
            settings.DATABASE_URI,
            app_modules={"models": ["app.hello.repository.message"]},
            testing=settings.APP_ENV == "testing",
            connection_label="models",
        )
        application.container = container

        container.wire(
            modules=[
                __name__,
                "app.hello.endpoints",
            ]
        )
        logger.info("Container Wiring complete")
        async with RegisterTortoise(
            app=application,
            config=config,
            generate_schemas=True,
            add_exception_handlers=True,
        ):
            logger.info("Tortoise ORM registered")
            yield
        logger.info("Shutting down application")
        await Tortoise.close_connections()
        logger.info("Tortoise ORM connections closed")
        logger.info("Application shutdown complete")

    app = FastAPI(
        title="FooBar Backend API",
        lifespan=lifespan,
        docs_url="/api/docs",
        redoc_url=None,
        debug=settings.APP_ENV == "development" or settings.APP_ENV == "testing",
    )
    return app


container = AppContainers()
server = bootstrap()

server.include_router(auth_router)
