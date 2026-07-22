import os
import tempfile
import pytest
from app.services.prompt_service import PromptService


class TestPromptService:
    def test_get_prompts_path(self):
        """Test getting prompts path for a project."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = PromptService(tmp_dir)
            
            expected_path = os.path.join(tmp_dir, "test-project", "story", "prompts")
            actual_path = service.get_prompts_path("test-project")
            assert actual_path == expected_path
    
    def test_get_prompt_file_path(self):
        """Test getting prompt file path for a scene."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = PromptService(tmp_dir)
            
            expected_path = os.path.join(tmp_dir, "test-project", "story", "prompts", "prompt_1.json")
            actual_path = service.get_prompt_file_path("test-project", 1)
            assert actual_path == expected_path
    
    def test_read_missing_prompt(self):
        """Test reading a prompt that doesn't exist."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = PromptService(tmp_dir)
            
            # Read non-existent prompt should return None
            content = service.read_prompt("test-project", 1)
            assert content is None
    
    def test_save_and_read_prompt(self):
        """Test saving and reading a prompt."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = PromptService(tmp_dir)
            
            # Save a prompt
            content_to_save = "This is the project story prompt.\nIt has multiple lines."
            result = service.save_prompt("test-project", 1, content_to_save)
            assert result is True
            
            # Read the saved prompt
            read_content = service.read_prompt("test-project", 1)
            assert read_content is not None
            assert read_content['content'] == content_to_save
    
    def test_read_all_prompts_empty(self):
        """Test reading all prompts when none exist."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = PromptService(tmp_dir)
            
            # Should return empty list for non-existent project
            prompts = service.read_all_prompts("non-existent-project")
            assert prompts == []
    
    def test_save_prompt_creates_directories(self):
        """Test that saving a prompt creates necessary directories."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = PromptService(tmp_dir)
            
            # Save prompt to a non‑existent directory path
            content_to_save = "Prompt content in nested directory"
            result = service.save_prompt("test-project", 1, content_to_save)
            assert result is True
            
            # Verify the file was created with correct content
            read_content = service.read_prompt("test-project", 1)
            assert read_content is not None
            assert read_content['content'] == content_to_save
    
    def test_generate_prompts_from_scenes_empty(self):
        """Test generating prompts from empty scenes."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = PromptService(tmp_dir)
            
            # Generate prompts from empty scenes should return empty list
            prompts = service.generate_prompts_from_scenes("test-project")
            assert prompts == []
    
    def test_generate_deterministic_prompt(self):
        """Test that prompt generation is deterministic."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = PromptService(tmp_dir)
            
            # Test simple scene content
            scene_content = "## Scene 1: Introduction\n\nThis is the introduction scene."
            result1 = service.generate_prompt_from_scene(scene_content, 1)
            result2 = service.generate_prompt_from_scene(scene_content, 1)
            
            assert result1 == result2
    
    def test_generate_prompts_from_scenes_with_content(self):
        """Test generating prompts from actual scene content."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # First create some scenes content
            from app.services.story_service import StoryService
            story_service = StoryService(tmp_dir)
            
            # Save some scenes first
            scenes_content = "# Scenes\n\n## Scene 1: Introduction\n\nThis is the introduction scene.\n\n## Scene 2: Conflict\n\nThis is a conflict scene."
            story_service.save_scenes("test-project", scenes_content)
            
            # Now test prompt generation from those scenes
            service = PromptService(tmp_dir)
            prompts = service.generate_prompts_from_scenes("test-project")
            
            assert len(prompts) == 2
            
            # Check first prompt
            assert prompts[0]['scene_number'] == 1
            assert "Scene 1: Introduction" in prompts[0]['content']
            assert "This is the introduction scene." in prompts[0]['content']
            
            # Check second prompt  
            assert prompts[1]['scene_number'] == 2
            assert "Scene 2: Conflict" in prompts[1]['content']
            assert "This is a conflict scene." in prompts[1]['content']
    
    def test_read_all_prompts_with_existing_prompts(self):
        """Test reading all prompts when they exist."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            service = PromptService(tmp_dir)
            
            # Save some prompts first
            service.save_prompt("test-project", 1, "Prompt content for scene 1")
            service.save_prompt("test-project", 2, "Prompt content for scene 2")
            
            # Read all prompts
            prompts = service.read_all_prompts("test-project")
            
            assert len(prompts) == 2
            
            # Check first prompt
            assert prompts[0]['scene_number'] == 1
            assert prompts[0]['content'] == "Prompt content for scene 1"
            
            # Check second prompt
            assert prompts[1]['scene_number'] == 2
            assert prompts[1]['content'] == "Prompt content for scene 2"
    
    # ------------------------------------------------------------------
    # New focused tests for context building and template engine usage
    # ------------------------------------------------------------------
    def test_build_prompt_context_with_title(self):
        """Ensure _build_prompt_context extracts title correctly."""
        service = PromptService()
        scene_content = "## Scene 1: The Beginning\nSome description."
        ctx = service._build_prompt_context(scene_content, 5)
        assert ctx['scene_number'] == '5'
        assert ctx['scene_title'] == "## Scene 1: The Beginning"
        # project_slug is empty string by design
        assert ctx['project_slug'] == ''
    
    def test_build_prompt_context_without_title(self):
        """Ensure context handles missing title gracefully."""
        service = PromptService()
        scene_content = "No heading here, just text."
        ctx = service._build_prompt_context(scene_content, 3)
        # Title should remain empty string when no heading exists
        assert ctx['scene_number'] == '3'
        assert ctx['scene_title'] == ""
    
    def test_generate_prompt_receives_correct_context(self):
        """Verify that PromptTemplateEngine receives the expected context."""
        service = PromptService()
        captured = {}
        
        original_render = service._template_engine.render
        
        def mock_render(template, ctx):
            captured['template'] = template
            captured['context'] = ctx
            # Delegate to the original render implementation
            return original_render(template, ctx)
    
        service._template_engine.render = mock_render
    
        scene_content = "## Scene X: Title\nContent with {{placeholder}}."
        result = service.generate_prompt_from_scene(scene_content, 2)
    
        # The render method should have been called once
        assert 'template' in captured
        assert 'context' in captured
        # Context should match what _build_prompt_context would produce
        expected_ctx = service._build_prompt_context(scene_content, 2)
        assert captured['context'] == expected_ctx
        # Verify that the rendered output contains the expanded scene title
        assert "## Scene X: Title" in result
    
    # ------------------------------------------------------------------
    # New tests for image and narration prompt generation
    # ------------------------------------------------------------------
    def test_generate_image_prompt(self):
        """Verify generate_image_prompt uses IMAGE_PROMPT_TEMPLATE."""
        service = PromptService()
        scene_content = "## Scene 1: Sunset\nA beautiful sunset over the hills."
        result = service.generate_image_prompt(scene_content, 1)
        assert "Image Prompt for" in result
        assert "Scene 1: Sunset" in result
        assert "A beautiful sunset over the hills." in result
    
    def test_generate_narration_prompt(self):
        """Verify generate_narration_prompt uses NARRATION_PROMPT_TEMPLATE."""
        service = PromptService()
        scene_content = "## Scene 2: Battle\nThe battle rages on."
        result = service.generate_narration_prompt(scene_content, 2)
        assert "Narration Prompt for" in result
        assert "Scene 2: Battle" in result
        assert "The battle rages on." in result
