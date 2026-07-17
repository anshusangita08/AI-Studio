#!/usr/bin/env python3

import os
import sys
from pathlib import Path

# Add the app directory to Python path so we can import modules
sys.path.insert(0, str(Path(__file__).parent))

try:
    from app.services.story_service import StoryService
    from app.services.project_service import ProjectService
    
    # Create instances 
    project_service = ProjectService()
    
    print("=== Debugging Scene File Handling ===")
    
    # Test what paths are being constructed
    slug = "test-project"
    
    try:
        project_path = project_service.get_project_path(slug)
        print(f"Project path for '{slug}': {project_path}")
        
        scenes_md_path = os.path.join(project_path, "scenes.md")
        print(f"Scenes MD path: {scenes_md_path}")
        
        # Check if directory exists
        if os.path.exists(project_path):
            print("✓ Project directory exists")
            
            # List contents of project dir
            print("Project directory contents:")
            for item in os.listdir(project_path):
                print(f"  {item}")
                
            # Create a test file to see if we can write
            test_content = "# Test Scenes\nThis is a test.\n"
            try:
                with open(scenes_md_path, 'w') as f:
                    f.write(test_content)
                print("✓ Successfully wrote test scenes.md")
                
                # Read it back
                with open(scenes_md_path, 'r') as f:
                    content = f.read()
                print(f"✓ Read back content: {repr(content)}")
                
            except Exception as e:
                print(f"✗ Failed to write/read file: {e}")
        else:
            print("✗ Project directory does NOT exist")
            
    except Exception as e:
        print(f"Error getting project path: {e}")

except ImportError as e:
    print(f"Import error: {e}")
except Exception as e:
    print(f"General error: {e}")