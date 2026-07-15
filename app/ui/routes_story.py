"""
Story routes.
"""

from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter
from fastapi import Form
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services.project_service import PROJECT_ROOT
from app.services.project_service import project_service
from app.services.story_service import StoryService

router = APIRouter(
    prefix="/projects",
    tags=["Story"],
)

templates = Jinja2Templates(
    directory="app/ui/templates",
)

story_service = StoryService(PROJECT_ROOT)


@router.get("/{slug}/story")
async def story_editor(
    request: Request,
    slug: str,
):
    try:
        project = project_service.get(slug)

    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        ) from exc

    return templates.TemplateResponse(
        request=request,
        name="story/editor.html",
        context={
            "title": f"{project.name} - Story",
            "project": project,
            "story": story_service.load(slug),
            "saved": False,
        },
    )


@router.post("/{slug}/story")
async def save_story(
    request: Request,
    slug: str,
    story: str = Form(...),
):
    try:
        project = project_service.get(slug)

    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        ) from exc

    story_service.save(
        slug,
        story,
    )

    return templates.TemplateResponse(
        request=request,
        name="story/editor.html",
        context={
            "title": f"{project.name} - Story",
            "project": project,
            "story": story,
            "saved": True,
        },
    )