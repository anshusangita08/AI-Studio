import os
import json
from pathlib import Path
from typing import List, Dict, Optional
import re

# Import the PromptTemplateEngine for placeholder rendering
from app.services.prompt_template_engine import PromptTemplateEngine
# Import the shared prompt templates
from app.services.prompt_templates import (
    PROMPT_TEMPLATE,
    IMAGE_PROMPT_TEMPLATE,
    NARRATION_PROMPT_TEMPLATE,
    STORY_EXPANSION_TEMPLATE,
    SCENES_GENERATION_TEMPLATE,
)
# Import LMStudioClient to enable prompt execution
from app.core.lm_studio_client import LMStudioClient


class PromptService:
    """Service for managing project prompts."""
    
    # Use the shared prompt template from prompt_templates module
    _PROMPT_TEMPLATE = PROMPT_TEMPLATE
    
    def __init__(self, projects_dir: str = "workspace/projects"):
        self.projects_dir = projects_dir
        # Instantiate the template engine once per service instance
        self._template_engine = PromptTemplateEngine()
        # Instantiate LMStudioClient for future prompt execution
        self._lm_client = LMStudioClient()
    
    def get_prompts_path(self, slug: str) -> str:
        """Get the path to the prompts directory for a given project slug."""
        return os.path.join(self.projects_dir, slug, "story", "prompts")
    
    def get_prompt_file_path(self, slug: str, scene_number: int) -> str:
        """Get the path to a specific prompt file for a scene."""
        prompts_dir = self.get_prompts_path(slug)
        return os.path.join(prompts_dir, f"prompt_{scene_number}.json")
    
    def read_prompt(self, slug: str, scene_number: int) -> Optional[Dict]:
        """
        Read a specific prompt content for a given project and scene number.
        
        Args:
            slug (str): The project slug
            scene_number (int): The scene number
            
        Returns:
            Dict: The prompt data or None if file doesn't exist
        """
        prompt_path = self.get_prompt_file_path(slug, scene_number)
        content = self._read_text_file(prompt_path)
        if not content:
            return None
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return None
    
    def read_all_prompts(self, slug: str) -> List[Dict]:
        """
        Read all prompts for a given project.
        
        Args:
            slug (str): The project slug
            
        Returns:
            List[Dict]: List of prompt dictionaries
        """
        prompts_dir = self.get_prompts_path(slug)
        prompts = []
        
        if not os.path.exists(prompts_dir):
            return prompts
            
        # Find all prompt files in the directory
        for filename in sorted(os.listdir(prompts_dir)):
            if filename.startswith("prompt_") and filename.endswith(".json"):
                try:
                    scene_number = int(filename.replace("prompt_", "").replace(".json", ""))
                    
                    content = self._read_text_file(os.path.join(prompts_dir, filename))
                    prompt_data = json.loads(content) if content else {}
                        
                    prompts.append({
                        'scene_number': scene_number,
                        'content': prompt_data.get('content', ''),
                        'project_slug': slug
                    })
                except (ValueError, json.JSONDecodeError):
                    # Skip invalid files
                    continue
                    
        return prompts
    
    def save_prompt(self, slug: str, scene_number: int, content: str) -> bool:
        """
        Save a prompt for a given project and scene number.
        
        Args:
            slug (str): The project slug
            scene_number (int): The scene number
            content (str): The prompt content to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        prompt_path = self.get_prompt_file_path(slug, scene_number)
        try:
            # Ensure the directory exists
            Path(prompt_path).parent.mkdir(parents=True, exist_ok=True)
            
            # Create prompt data structure
            prompt_data = {
                'content': content,
                'project_slug': slug,
                'scene_number': scene_number
            }
            
            with open(prompt_path, 'w', encoding='utf-8') as f:
                json.dump(prompt_data, f, ensure_ascii=False, indent=2)
            return True
        except (OSError, IOError):
            return False
    
    def generate_prompts_from_scenes(self, slug: str) -> List[Dict]:
        """
        Generate structured prompts from existing scenes.
        
        Args:
            slug (str): The project slug
            
        Returns:
            List[Dict]: Generated prompt dictionaries
        """
        # Read the scenes content directly from filesystem
        scenes_content = self._read_scenes_for_prompt_generation(slug)
        
        if not scenes_content.strip():
            return []
            
        # Split into individual scene sections
        scene_sections = self._split_scenes(scenes_content)
        
        prompts = []
        for i, section in enumerate(scene_sections):
            if not section.strip():
                continue
                
            scene_number = i + 1
            
            # Generate a deterministic prompt based on the scene content
            prompt_content = self.generate_prompt_from_scene(section, scene_number)
            
            prompts.append({
                'content': prompt_content,
                'project_slug': slug,
                'scene_number': scene_number
            })
        
        return prompts
    
    def _read_scenes_for_prompt_generation(self, slug: str) -> str:
        """Read scenes content for prompt generation."""
        # Read scenes file directly from filesystem instead of instantiating StoryService
        scenes_path = os.path.join(self.projects_dir, slug, "story", "scenes.md")
        
        if not os.path.exists(scenes_path):
            return ""
            
        return self._read_text_file(scenes_path)
    
    def _split_scenes(self, scenes_content: str) -> List[str]:
        """Split scenes content into individual scene sections."""
        # Find all "## Scene" headings with their positions
        pattern = r'(##\s+Scene\s+\d+(?:[:\s].*?)?\n)'
        
        # Use finditer to get all matches with their start/end positions
        matches = list(re.finditer(pattern, scenes_content))
        
        if not matches:
            return [scenes_content.strip()]
            
        # Extract scene sections from one heading to the next
        result = []
        for i, match in enumerate(matches):
            start_pos = match.start()
            
            # For the last scene, slice to end of string
            if i == len(matches) - 1:
                section = scenes_content[start_pos:].strip()
            else:
                # Slice from current heading to next heading
                next_start = matches[i + 1].start()
                section = scenes_content[start_pos:next_start].strip()
            
            if section:
                result.append(section)
                
        return result
    
    def generate_prompt_from_scene(self, scene_content: str, scene_number: int) -> str:
        """
        Generate a deterministic prompt from scene content.
        
        Args:
            scene_content (str): The raw scene content
            scene_number (int): Scene number for context
            
        Returns:
            str: Generated prompt content
        """
        return self._render_prompt(self._PROMPT_TEMPLATE, scene_content, scene_number)
    
    # New public methods for image and narration prompts
    def generate_image_prompt(self, scene_content: str, scene_number: int) -> str:
        """Generate an image prompt using IMAGE_PROMPT_TEMPLATE."""
        context = self._image_context(scene_content, scene_number)
        return self._render_prompt(IMAGE_PROMPT_TEMPLATE, context)
    
    def generate_narration_prompt(self, scene_content: str, scene_number: int) -> str:
        """Generate a narration prompt using NARRATION_PROMPT_TEMPLATE."""
        context = self._narration_context(scene_content, scene_number)
        return self._render_prompt(NARRATION_PROMPT_TEMPLATE, context)
    
    # Private helper to render any template with context
    def _render_prompt(self, template: str, content_or_context, scene_number: int = None) -> str:
        """
        Render a prompt using the given template and scene data.
        
        Builds the rendering context via _build_prompt_context (or uses provided dict)
        and delegates to PromptTemplateEngine.
        """
        if isinstance(content_or_context, dict):
            # Already a full context
            context = content_or_context
        else:
            # Build context from scene content
            context = self._build_prompt_context(content_or_context, scene_number)
        return self._template_engine.render(template, context)
    
    def _image_context(self, scene_content: str, scene_number: int) -> Dict[str, str]:
        """
        Build image prompt context by extending the base context with default values.
        """
        base = self._build_prompt_context(scene_content, scene_number)
        # Add fixed defaults for image prompts
        base.update({
            'visual_style': "Cinematic realism",
            'composition': "Wide establishing shot",
            'lighting': "Natural scene lighting",
            'camera': "35mm cinematic",
            'quality': "Highly detailed",
            'negative_prompt': "Low quality, blurry, watermark, text"
        })
        return base
    
    def _narration_context(self, scene_content: str, scene_number: int) -> Dict[str, str]:
        """
        Build narration prompt context by extending the base context with default values.
        """
        base = self._build_prompt_context(scene_content, scene_number)
        # Add fixed defaults for narration prompts
        base.update({
            'narration_style': "Cinematic storytelling",
            'tone': "Immersive",
            'pacing': "Moderate",
            'voice_style': "Warm and expressive",
            'target_duration': "30-60 seconds",
            'delivery_notes': "Natural pacing with emotional emphasis"
        })
        return base
    
    def _build_prompt_context(self, scene_content: str, scene_number: int) -> Dict[str, str]:
        """
        Build a context dictionary for rendering placeholders.
        
        Includes:
          - project_slug (empty string if not available)
          - scene_number
          - scene_title (if present; otherwise empty string)
          - scene_content
        
        Missing values resolve to empty strings.
        """
        # Extract title from the first heading line if it exists
        title = ""
        for line in scene_content.splitlines():
            if line.startswith('##'):
                title = line.strip()
                break
        
        return {
            'project_slug': '',
            'scene_number': str(scene_number),
            'scene_title': title,
            'scene_content': scene_content
        }
    
    # New helper method for pipeline status
    def are_prompts_complete(self, slug: str) -> bool:
        """
        Return True if at least one non‑empty prompt file exists.
        """
        prompts_dir = self.get_prompts_path(slug)
        if not os.path.exists(prompts_dir):
            return False
        for filename in os.listdir(prompts_dir):
            if filename.endswith(".json"):
                path = os.path.join(prompts_dir, filename)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    if content.strip():
                        return True
                except OSError:
                    continue
        return False
    
    # ------------------------------------------------------------------
    # Prompt execution helper (integrates LMStudioClient)
    # ------------------------------------------------------------------
    
    def execute(self, rendered_prompt: str) -> str:
        """
        Public wrapper for executing a rendered prompt.
        
        Delegates to the private _execute_prompt method.
        """
        return self._execute_prompt(rendered_prompt)
    
    def _read_text_file(self, path: str) -> str:
        """
        Read the entire contents of a text file using UTF‑8 encoding.

        Returns an empty string if the file cannot be read (e.g., missing or
        permission error).  This helper is used internally to avoid duplicating
        the open/read/close pattern across multiple methods.
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except (OSError, IOError):
            return ""

    def _execute_prompt(self, rendered_prompt: str) -> str:
        """
        Execute a rendered prompt using the LMStudioClient.
        
        Parameters:
            rendered_prompt (str): The fully rendered prompt text.
            
        Returns:
            str: The generated response from LM Studio.
            
        Raises:
            LMStudioError or its subclasses – propagates any exception
            raised by LMStudioClient.generate_text.
        """
        # Use the existing LMStudioClient instance to generate text
        return self._lm_client.generate_text(rendered_prompt)
    
    # ------------------------------------------------------------------
    # NEW PUBLIC API: Generate a complete story for a project
    # ------------------------------------------------------------------
    
    def generate_story(self, slug: str) -> str:
        """
        Generate a full expanded story for the given project slug.

        The method:
          1. Reads the original story from workspace/projects/<slug>/story/story.md.
          2. Renders STORY_EXPANSION_TEMPLATE using the story content.
          3. Executes the rendered prompt via LMStudioClient.
          4. Returns the generated expanded story text.

        Returns an empty string if the story file does not exist or is empty.
        """
        # Path to the original story file
        story_path = os.path.join(self.projects_dir, slug, "story", "story.md")
        if not os.path.exists(story_path):
            return ""

        story_content = self._read_text_file(story_path)

        if not story_content.strip():
            return ""

        # Render the expansion prompt
        rendered_prompt = self._render_prompt(STORY_EXPANSION_TEMPLATE, {'story': story_content})

        # Execute the prompt and return the result
        return self.execute(rendered_prompt)

    # ------------------------------------------------------------------
    # New method: Generate scenes from expanded story
    # ------------------------------------------------------------------

    def generate_scenes_from_expanded_story(self, slug: str) -> str:
        """
        Generate scenes from the expanded story for the given project slug.

        Reads expanded_story.md, renders SCENES_GENERATION_TEMPLATE, executes via LMStudioClient,
        and returns the generated scenes text.

        Returns an empty string if expanded_story.md does not exist or is empty.
        """
        expanded_path = os.path.join(self.projects_dir, slug, "story", "expanded_story.md")
        if not os.path.exists(expanded_path):
            return ""
        expanded_story = self._read_text_file(expanded_path)
        if not expanded_story.strip():
            return ""

        rendered_prompt = self._render_prompt(SCENES_GENERATION_TEMPLATE, {'expanded_story': expanded_story})
        return self.execute(rendered_prompt)
    
