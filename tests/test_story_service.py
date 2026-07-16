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