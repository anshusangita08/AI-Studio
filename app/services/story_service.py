import os
from pathlib import Path
import re

# Import PromptService for story generation
from app.services.prompt_service import PromptService


class StoryService:
    """Service for managing project stories."""
    
    # ------------------------------------------------------------------
    # Private helper methods for file I/O
    # ------------------------------------------------------------------
    def _read_text_file(self, path: str) -> str:
        """Read the entire contents of a text file."""
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def _write_text_file(self, path: str, content: str) -> None:
        """Write the given content to a text file."""
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    def __init__(self, projects_dir: str = "workspace/projects"):
        self.projects_dir = projects_dir
        # Instantiate PromptService once with the same projects_dir
        self._prompt_service = PromptService(projects_dir)

    # ------------------------------------------------------------------
    # Private helpers for path construction
    # ------------------------------------------------------------------
    def _project_dir(self, slug: str) -> str:
        """Return the absolute directory path for a project."""
        return os.path.join(self.projects_dir, slug)
    
    def _story_dir(self, slug: str) -> str:
        """Return the story sub‑directory path for a project."""
        return os.path.join(self._project_dir(slug), "story")
    
    def get_story_path(self, slug: str) -> str:
        """Get the path to a story file for a given project slug."""
        return os.path.join(self._story_dir(slug), "story.md")
    
    def get_expanded_story_path(self, slug: str) -> str:
        """Get the path to an expanded story file for a given project slug."""
        return os.path.join(self._story_dir(slug), "expanded_story.md")
    
    def read_story(self, slug: str) -> str:
        story_path = self.get_story_path(slug)
        if os.path.exists(story_path):
            return self._read_text_file(story_path)
        return ""

    def read_expanded_story(self, slug: str) -> str:
        expanded_path = self.get_expanded_story_path(slug)
        if os.path.exists(expanded_path):
            return self._read_text_file(expanded_path)
        return ""
    
    def save_story(self, slug: str, content: str) -> bool:
        story_path = self.get_story_path(slug)
        try:
            Path(story_path).parent.mkdir(parents=True, exist_ok=True)
            self._write_text_file(story_path, content)
            return True
        except (OSError, IOError):
            return False
            
    def save_expanded_story(self, slug: str, content: str) -> bool:
        expanded_path = self.get_expanded_story_path(slug)
        try:
            Path(expanded_path).parent.mkdir(parents=True, exist_ok=True)
            self._write_text_file(expanded_path, content)
            return True
        except (OSError, IOError):
            return False
            
    def get_scenes_path(self, slug: str) -> str:
        """Get the path to a scenes file for a given project slug."""
        return os.path.join(self._story_dir(slug), "scenes.md")
    
    def read_scenes(self, slug: str) -> str:
        """
        Read the scenes content for a given project slug.
        
        Args:
            slug (str): The project slug
            
        Returns:
            str: The scenes content or empty string if file doesn't exist
        """
        scenes_path = self.get_scenes_path(slug)
        if os.path.exists(scenes_path):
            with open(scenes_path, 'r', encoding='utf-8') as f:
                return f.read()
        return ""
    
    def save_scenes(self, slug: str, content: str) -> bool:
        scenes_path = self.get_scenes_path(slug)
        try:
            Path(scenes_path).parent.mkdir(parents=True, exist_ok=True)
            self._write_text_file(scenes_path, content)
            return True
        except (OSError, IOError):
            return False
            
    def generate_mock_scenes(self, expanded_story: str) -> str:
        """
        Generate deterministic placeholder scenes content from expanded story.
        
        Args:
            expanded_story (str): The expanded story content to generate scenes from
            
        Returns:
            str: Generated scenes content
        """
        if not expanded_story.strip():
            return "# Scenes\n\nNo scenes generated. Please provide an expanded story."
        
        # Simple deterministic scene generation based on the expanded story
        lines = expanded_story.split('\n')
        scenes_content = ["# Scenes", ""]
        
        # Add some example scenes structure - maintaining original test format compatibility
        scenes_content.append("## Scene 1: Introduction")
        scenes_content.append("- Setting: [Setting from expanded story]")
        scenes_content.append("- Characters: [Main characters from expanded story]") 
        scenes_content.append("- Objective: [Primary goal from expanded story]")
        scenes_content.append("")
        
        # Add some more example scenes
        scenes_content.append("## Scene 2: Conflict")
        scenes_content.append("- Problem encountered")
        scenes_content.append("- Character reactions")
        scenes_content.append("- Plot twist (if any)")
        scenes_content.append("")
        
        scenes_content.append("## Scene 3: Resolution")
        scenes_content.append("- How problem is solved")
        scenes_content.append("- Character growth")
        scenes_content.append("- Ending notes")
        scenes_content.append("")
        
        # Add a note about where the generated scenes might come from
        scenes_content.append("---")
        scenes_content.append("Note: These are placeholder scenes. In a real implementation, these would be:")
        scenes_content.append("- Generated based on story elements and plot structure")
        scenes_content.append("- Split into more specific scene breakdowns")
        scenes_content.append("- Connected to character arcs and theme development")
        
        return '\n'.join(scenes_content)

    def generate_mock_story(self, project_name):
        """Generate deterministic placeholder story content for a given project name."""
        # Reuse the single PromptService instance
        return self._prompt_service.generate_story(project_name)

    # New helper methods for pipeline status
    def is_story_complete(self, slug: str) -> bool:
        """
        Return True if a non‑empty story file exists.
        """
        path = self.get_story_path(slug)
        if not os.path.exists(path):
            return False
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        return bool(content)

    def are_scenes_complete(self, slug: str) -> bool:
        """
        Return True if a non‑empty scenes file exists and contains at least one scene heading.
        """
        path = self.get_scenes_path(slug)
        if not os.path.exists(path):
            return False
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Simple check for "## Scene" headings using multiline regex
        pattern = r'^##\s+Scene\b'
        return bool(re.search(pattern, content, flags=re.MULTILINE))
