"""
Project routes.
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import Form
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services.project_service import project_service

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)

templates = Jinja2Templates(
    directory="app/ui/templates",
)


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
async def create_project(
    request: Request,
    name: str = Form(...),
):
    try:
        project = project_service.create(name)
        
        return RedirectResponse(
            url=f"/projects/{project.slug}",
            status_code=303,
        )
    
    except (ValueError, FileExistsError) as exc:
        # Return to the creation page with error message
        return templates.TemplateResponse(
            request=request,
            name="projects/create.html",
            context={
                "title": "Create Project",
                "error": str(exc),
            },
        )


@router.get("/{slug}")
async def open_project(
    request: Request,
    slug: str,
):
    try:
        project = project_service.get(slug)
        pipeline_status = project_service.get_pipeline_status(project.slug)

        # Calculate completion metrics
        completed = sum([
            1 if pipeline_status["story_complete"] else 0,
            1 if pipeline_status["scenes_complete"] else 0,
            1 if pipeline_status["prompts_complete"] else 0,
        ])
        percent = (completed / 3) * 100

        # Store metrics in the status dict
        pipeline_status["completed"] = completed
        pipeline_status["percent"] = percent

    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        ) from exc

    return templates.TemplateResponse(
        request=request,
        name="projects/details.html",
        context={
            "title": project.name,
            "project": project,
            "pipeline_status": pipeline_status,
        },
    )


@router.post("/{slug}/rename")
async def rename_project(
    slug: str,
    name: str = Form(...),
):
    try:
        project = project_service.rename(
            slug,
            name,
        )

    except (FileNotFoundError, ValueError, FileExistsError) as exc:
        raise HTTPException(
            status_code=404 if isinstance(exc, FileNotFoundError) else 400,
            detail=str(exc),
        ) from exc

    return RedirectResponse(
        url=f"/projects/{project.slug}",
        status_code=303,
    )


@router.post("/{slug}/delete")
async def delete_project(
    slug: str,
):
    try:
        project_service.delete(slug)

    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        ) from exc

    return RedirectResponse(
        url="/projects/",
        status_code=303,
    )


@router.post("/{slug}/export")
async def export_project(
    slug: str,
):
    try:
        project_service.export_project(slug)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        ) from exc

    return RedirectResponse(
        url=f"/projects/{slug}",
        status_code=303,
    )


# ------------------------------------------------------------------
# New route for rendering a project
# ------------------------------------------------------------------
@router.post("/{slug}/render")
async def render_project(
    slug: str,
):
    """
    Render the specified project.

    This endpoint simply delegates to `project_service.render_project`
    and returns the JSON response from the underlying RenderService.
    """
    try:
        # Delegate rendering logic to ProjectService
        render_response = project_service.render_project(slug)
    except FileNotFoundError as exc:
        # Consistent error handling with other routes
        raise HTTPException(status_code=404, detail=str(exc))
    except Exception as exc:
        # Generic fallback for unexpected errors
        raise HTTPException(status_code=500, detail=str(exc))

    return {"success": True, "render_result": render_response}
