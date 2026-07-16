import os
from pathlib import Path


class StoryService:
    """Service for managing project stories."""
    
    def __init__(self, projects_dir: str = "workspace/projects"):
        self.projects_dir = projects_dir
    
    def get_story_path(self, slug: str) -> str:
        """Get the path to a story file for a given project slug."""
        return os.path.join(self.projects_dir, slug, "story", "story.md")
    
    def read_story(self, slug: str) -> str:
        """
        Read the story content for a given project slug.
        
        Args:
            slug (str): The project slug
            
        Returns:
            str: The story content or empty string if file doesn't exist
        """
        story_path = self.get_story_path(slug)
        if os.path.exists(story_path):
            with open(story_path, 'r', encoding='utf-8') as f:
                return f.read()
        return ""
    
    def save_story(self, slug: str, content: str) -> bool:
        """
        Save story content for a given project slug.
        
        Args:
            slug (str): The project slug
            content (str): The story content to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        story_path = self.get_story_path(slug)
        try:
            # Ensure the directory exists
            Path(story_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(story_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception:
            return False