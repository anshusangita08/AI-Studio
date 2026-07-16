from fastapi import APIRouter, Depends, Request, HTTPException, Form
from app.services.project_service import project_service
from app.services.story_service import StoryService
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/projects", tags=["story"])

story_service = StoryService()
templates = Jinja2Templates(directory="app/ui/templates")

@router.get("/{slug}/story")
async def get_story(slug: str, request: Request):
    """Get story content for a project."""
    try:
        project = project_service.get(slug)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Project not found")
        
    story_content = story_service.read_story(slug)
    expanded_story_content = story_service.read_expanded_story(slug)
    
    return templates.TemplateResponse(
        request=request,
        name="projects/story.html",
        context={
            "project": project,
            "story_content": story_content,
            "expanded_story_content": expanded_story_content
        }
    )

@router.post("/{slug}/story/generate")
async def generate_story(
    slug: str, 
    request: Request
):
    """Generate mock story content for a project."""
    try:
        project = project_service.get(slug)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Project not found")
        
    # Generate mock story content (this will populate the expanded story field)
    generated_content = story_service.generate_mock_story(project.name)
    
    # For AJAX requests, return just the content
    if request.headers.get("content-type", "").startswith("application/json"):
        return {"expanded_story": generated_content}
    
    return templates.TemplateResponse(
        request=request,
        name="projects/story.html",
        context={
            "project": project,
            "story_content": "",  # Keep original unchanged
            "expanded_story_content": generated_content  # Populate expanded field only
        }
    )

@router.post("/{slug}/story")
async def save_story(
    slug: str, 
    request: Request,
    content: str = Form(...)
):
    """Save story content for a project."""
    try:
        project = project_service.get(slug)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Project not found")
        
    success = story_service.save_story(slug, content)
    
    if not success:
        raise HTTPException(status_code=500, detail="Failed to save story")
        
    return RedirectResponse(
        url=f"/projects/{slug}/story",
        status_code=303
    )

@router.post("/{slug}/expanded-story")
async def save_expanded_story(
    slug: str, 
    request: Request,
    content: str = Form(...)
):
    """Save expanded story content for a project."""
    try:
        project = project_service.get(slug)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Project not found")
        
    success = story_service.save_expanded_story(slug, content)
    
    if not success:
        raise HTTPException(status_code=500, detail="Failed to save expanded story")
        
    return RedirectResponse(
        url=f"/projects/{slug}/story",
        status_code=303
    )
