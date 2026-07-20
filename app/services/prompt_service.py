import os
import json
from pathlib import Path
from typing import List, Dict, Optional
import re


class PromptService:
    """Service for managing project prompts."""
    
    def __init__(self, projects_dir: str = "workspace/projects"):
        self.projects_dir = projects_dir
    
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
        if os.path.exists(prompt_path):
            with open(prompt_path, 'r', encoding='utf-8') as f:
                return json.load(f)
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
                    
                    with open(os.path.join(prompts_dir, filename), 'r', encoding='utf-8') as f:
                        prompt_data = json.load(f)
                        
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
            
        try:
            with open(scenes_path, 'r', encoding='utf-8') as f:
                return f.read()
        except (OSError, IOError):
            return ""
    
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
        # Simple deterministic generation based on scene structure
        lines = scene_content.strip().split('\n')
        
        # Extract title if it exists
        title_line = ""
        if len(lines) > 0 and lines[0].startswith('##'):
            title_line = lines[0]
            
        # Create a structured prompt template
        prompt_lines = [
            f"# Prompt for {title_line.strip() if title_line else f'Scene {scene_number}'}",
            "",
            "## Task Description",
            "Generate content based on the following scene description:",
            "",
            scene_content,
            "",
            "## Instructions",
            "- Follow the structure and key elements from the scene description",
            "- Maintain consistency with the overall story tone and style",
            "- Focus on the specific elements mentioned in this scene",
            "- Ensure the generated content aligns with the project's narrative direction",
            "",
            "## Output Format",
            "Provide your response in markdown format.",
            ""
        ]
        
        return '\n'.join(prompt_lines)
