from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.bootstrap import bootstrap
from app.core.config import config
from app.core.logging import logger
from app.core.version import APP_NAME, VERSION
from app.ui.routes_projects import router as project_router
from app.ui.routes_story import router as story_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Starting AI Studio")

    bootstrap.initialize()

    yield

    logger.info("Stopping AI Studio")


app = FastAPI(
    title=APP_NAME,
    version=VERSION.full,
    lifespan=lifespan,
)

app.mount(
    "/static",
    StaticFiles(directory="app/ui/static"),
    name="static",
)

app.include_router(project_router)
app.include_router(story_router)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/version")
async def version():
    return {
        "application": APP_NAME,
        "version": VERSION.full,
    }


@app.get("/config")
async def configuration():
    return config.data