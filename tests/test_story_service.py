import os
import tempfile
import pytest
from app.services.story_service import StoryService


class TestStoryService:
    def test_read_missing_story(self):
        """Test reading a story that doesn't exist."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # Read non-existent story should return empty string
            content = service.read_story("test-project")
            assert content == ""
    
    def test_save_and_read_story(self):
        """Test saving and reading a story."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # Save a story
            content_to_save = "This is the project story content.\nIt has multiple lines."
            result = service.save_story("test-project", content_to_save)
            assert result is True
            
            # Read the saved story
            read_content = service.read_story("test-project")
            assert read_content == content_to_save
    
    def test_read_existing_story(self):
        """Test reading an existing story file."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # First save a story
            initial_content = "Initial story content"
            service.save_story("test-project", initial_content)
            
            # Then read it back
            read_content = service.read_story("test-project")
            assert read_content == initial_content
    
    def test_save_story_creates_directories(self):
        """Test that saving a story creates necessary directories."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # Save story to a non-existent directory path
            content_to_save = "Story content in nested directory"
            result = service.save_story("test-project", content_to_save)
            assert result is True
            
            # Verify the file was created with correct content
            read_content = service.read_story("test-project")
            assert read_content == content_to_save
    
    def test_get_story_path(self):
        """Test getting story path for a project."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            expected_path = os.path.join(tmp_dir, "test-project", "story", "story.md")
            actual_path = service.get_story_path("test-project")
            assert actual_path == expected_path
    
    def test_get_expanded_story_path(self):
        """Test getting expanded story path for a project."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            expected_path = os.path.join(tmp_dir, "test-project", "story", "expanded_story.md")
            actual_path = service.get_expanded_story_path("test-project")
            assert actual_path == expected_path
    
    def test_save_and_read_expanded_story(self):
        """Test saving and reading an expanded story."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # Save an expanded story
            content_to_save = "This is the expanded project story content.\nIt has multiple lines."
            result = service.save_expanded_story("test-project", content_to_save)
            assert result is True
            
            # Read the saved expanded story
            read_content = service.read_expanded_story("test-project")
            assert read_content == content_to_save
    
    def test_read_missing_expanded_story(self):
        """Test reading an expanded story that doesn't exist."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # Read non-existent expanded story should return empty string
            content = service.read_expanded_story("test-project")
            assert content == ""
    
    def test_save_expanded_story_creates_directories(self):
        """Test that saving an expanded story creates necessary directories."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # Save expanded story to a non-existent directory path
            content_to_save = "Expanded story content in nested directory"
            result = service.save_expanded_story("test-project", content_to_save)
            assert result is True
            
            # Verify the file was created with correct content
            read_content = service.read_expanded_story("test-project")
            assert read_content == content_to_save
    
    def test_generate_mock_story(self):
        """Test generate_mock_story method."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # Test generate_mock_story method
            result = service.generate_mock_story("Test Project")
            
            assert "Test Project" in result
            assert result.startswith("# Test Project")
            assert "mock story" in result.lower()
            
    def test_generate_mock_story_deterministic(self):
        """Test that generate_mock_story produces deterministic output."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # Generate twice with same input - should be identical
            result1 = service.generate_mock_story("Test Project")
            result2 = service.generate_mock_story("Test Project")
            
            assert result1 == result2
            
    def test_generate_mock_story_includes_project_name(self):
        """Test that generated content includes the project name."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # Test that generated content includes the project name
            project_name = "My Amazing Project"
            result = service.generate_mock_story(project_name)
            
            assert project_name in result
            
    def test_get_scenes_path(self):
        """Test that scenes path generation works."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            expected_path = os.path.join(tmp_dir, "test-project", "story", "scenes.md")
            actual_path = service.get_scenes_path("test-project")
            assert actual_path == expected_path
            
    def test_read_scenes(self):
        """Test reading scenes content."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # Test with non-existent file
            result = service.read_scenes("non-existent-project")
            assert result == ""
    
    def test_save_scenes(self):
        """Test saving scenes content."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # This should succeed without error (can't easily test actual file creation)
            success = service.save_scenes("test-project", "# Test Scenes\n\nScene 1 description.")
            assert success is True
            
    def test_generate_mock_scenes(self):
        """Test generating mock scenes from expanded story."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = StoryService(tmp_dir)
            
            # Test with empty content
            result_empty = service.generate_mock_scenes("")
            assert "No scenes generated" in result_empty
            
            # Test with normal content  
            expanded_story = "# Expanded Story\n\nThis is an expanded version.\n\nIt has more details."
            result = service.generate_mock_scenes(expanded_story)
            
            assert "# Scenes" in result
            assert "Scene 1: Introduction" in result
            assert "Scene 2: Conflict" in result  
            assert "Scene 3: Resolution" in result
