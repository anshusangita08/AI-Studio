"""
Project routes.
"""

from __future__ import annotations

from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services.project_service import project_service

router = APIRouter(prefix="/projects", tags=["Projects"])

templates = Jinja2Templates(directory="app/ui/templates")


@router.get("/")
async def list_projects(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="projects/index.html",
        context={
            "title": "Projects",
            "projects": project_service.list(),
        },
    )


@router.get("/new")
async def new_project(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="projects/create.html",
        context={
            "title": "Create Project",
        },
    )


@router.post("/new")
async def create_project(name: str = Form(...)):
    project_service.create(name)

    return RedirectResponse(
        url="/projects/",
        status_code=303,
    )