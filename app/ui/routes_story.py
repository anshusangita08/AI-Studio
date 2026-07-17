from fastapi import APIRouter, Depends, Request, HTTPException, Form
from app.services.project_service import project_service
from app.services.story_service import StoryService
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/projects", tags=["story"])

story_service = StoryService()
templates = Jinja2Templates(directory="app/ui/templates")

def _get_project_or_404(slug: str):
    """Helper function to get project or raise 404."""
    try:
        return project_service.get(slug)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Project not found")

def _build_story_context(project, slug):
    """Build common story context for templates."""
    return {
        "project": project,
        "story_content": story_service.read_story(slug),
        "expanded_story_content": story_service.read_expanded_story(slug),
        "scenes_content": story_service.read_scenes(slug)
    }

@router.get("/{slug}/story")
async def get_story(slug: str, request: Request):
    """Get story content for a project."""
    project = _get_project_or_404(slug)
    
    return templates.TemplateResponse(
        request=request,
        name="projects/story.html",
        context=_build_story_context(project, slug)
    )

@router.post("/{slug}/story/generate")
async def generate_story(
    slug: str, 
    request: Request
):
    """Generate mock story content for a project."""
    project = _get_project_or_404(slug)
    
    # Read the current expanded story
    expanded_story_content = story_service.read_expanded_story(slug)
    
    # Generate mock story content based on expanded story (this will populate the expanded story field)
    generated_content = story_service.generate_mock_story(expanded_story_content)
    
    # For AJAX requests, return just the content
    if request.headers.get("content-type", "").startswith("application/json"):
        return {"expanded_story": generated_content}
    
    context = _build_story_context(project, slug)
    context["story_content"] = ""  # Keep original unchanged
    context["expanded_story_content"] = generated_content  # Populate expanded field only
    
    return templates.TemplateResponse(
        request=request,
        name="projects/story.html",
        context=context
    )

@router.post("/{slug}/story")
async def save_story(
    slug: str, 
    request: Request,
    content: str = Form(...)
):
    """Save story content for a project."""
    _get_project_or_404(slug)
    
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
    _get_project_or_404(slug)
    
    success = story_service.save_expanded_story(slug, content)
    
    if not success:
        raise HTTPException(status_code=500, detail="Failed to save expanded story")
        
    return RedirectResponse(
        url=f"/projects/{slug}/story",
        status_code=303
    )

@router.post("/{slug}/scenes")
async def save_scenes(
    slug: str, 
    request: Request,
    content: str = Form(...)
):
    """Save scenes content for a project."""
    project = _get_project_or_404(slug)
    
    success = story_service.save_scenes(slug, content)
    
    if not success:
        raise HTTPException(status_code=500, detail="Failed to save scenes")
        
    # Reload the story page with updated scenes content
    scenes_content = story_service.read_scenes(slug)
    
    context = _build_story_context(project, slug)
    context["scenes_content"] = scenes_content

    return templates.TemplateResponse(
        request=request,
        name="projects/story.html",
        context=context
    )

@router.post("/{slug}/scenes/generate")
async def generate_scenes(
    slug: str, 
    request: Request
):
    """Generate mock scenes content for a project based on expanded story."""
    project = _get_project_or_404(slug)
    
    # Read the current expanded story
    expanded_story_content = story_service.read_expanded_story(slug)
    
    # Generate scenes from the expanded story content
    generated_scenes = story_service.generate_mock_scenes(expanded_story_content)
    
    # For AJAX requests, return just the content 
    if request.headers.get("content-type", "").startswith("application/json"):
        return {"scenes": generated_scenes}
    
    context = _build_story_context(project, slug)
    context["story_content"] = ""  # Keep original unchanged
    context["expanded_story_content"] = expanded_story_content  # Keep existing expanded story 
    context["scenes_content"] = generated_scenes  # Populate scenes field only
    
    return templates.TemplateResponse(
        request=request,
        name="projects/story.html",
        context=context
    )