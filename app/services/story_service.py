import os
from pathlib import Path


class StoryService:
    """Service for managing project stories."""
    
    def __init__(self, projects_dir: str = "workspace/projects"):
        self.projects_dir = projects_dir
    
    def get_story_path(self, slug: str) -> str:
        """Get the path to a story file for a given project slug."""
        return os.path.join(self.projects_dir, slug, "story", "story.md")
    
    def get_expanded_story_path(self, slug: str) -> str:
        """Get the path to an expanded story file for a given project slug."""
        return os.path.join(self.projects_dir, slug, "story", "expanded_story.md")
    
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
    
    def read_expanded_story(self, slug: str) -> str:
        """
        Read the expanded story content for a given project slug.
        
        Args:
            slug (str): The project slug
            
        Returns:
            str: The expanded story content or empty string if file doesn't exist
        """
        expanded_path = self.get_expanded_story_path(slug)
        if os.path.exists(expanded_path):
            with open(expanded_path, 'r', encoding='utf-8') as f:
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
            
    def save_expanded_story(self, slug: str, content: str) -> bool:
        """
        Save expanded story content for a given project slug.
        
        Args:
            slug (str): The project slug
            content (str): The expanded story content to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        expanded_path = self.get_expanded_story_path(slug)
        try:
            # Ensure the directory exists
            Path(expanded_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(expanded_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception:
            return False
            
    def get_scenes_path(self, slug: str) -> str:
        """Get the path to a scenes file for a given project slug."""
        return os.path.join(self.projects_dir, slug, "story", "scenes.md")
    
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
        """
        Save scenes content for a given project slug.
        
        Args:
            slug (str): The project slug
            content (str): The scenes content to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        scenes_path = self.get_scenes_path(slug)
        try:
            # Ensure the directory exists
            Path(scenes_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(scenes_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception:
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
        
        # Add some example scenes structure
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
        return f"# {project_name}\n\nThis is a mock story generated for the project '{project_name}'.\n\nThe story contains placeholders that would normally be generated by an AI model.\n\n## Story Elements\n\n- Character: Placeholder Hero\n- Setting: Unknown Location\n- Plot: Adventure awaits\n\nThis is placeholder content that will be replaced with actual AI-generated content in future implementations."
