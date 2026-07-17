#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import traceback

# Add the app directory to Python path so we can import modules
sys.path.insert(0, str(Path(__file__).parent))

try:
    from app.services.story_service import StoryService
    # Remove ProjectService import since it's not needed for scenes test
    import logging
    
    # Set up logging to see what's happening
    logging.basicConfig(level=logging.DEBUG)
    
    print("=== Detailed Scene File Debug ===")
    
    # Create instances 
    story_service = StoryService()
    
    slug = "test-project"
    
    try:
        # Test path resolution - we don't need project service for scenes
        scenes_path = story_service.get_scenes_path(slug)
        print(f"Scenes path for '{slug}': {scenes_path}")
        print(f"Absolute path: {os.path.abspath(scenes_path)}")
        
        scenes_md_path = scenes_path
        
        # Test saving with normal content first (this should work)
        test_content = "# Test Scenes\nScene 1 content here.\nScene 2 content here.\n"
        print(f"\nTesting save with content: {repr(test_content)}")
        
        # Let's capture what happens inside the actual method to see any exception
        import inspect
        save_method = story_service.save_scenes
        
        try:
            success = save_method(slug, test_content)
            print(f"Save result: {success}")
        except Exception as e:
            print("Exception directly from save_scenes call:")
            print(f"Error type: {type(e).__name__}") 
            print(f"Error message: {str(e)}")
            tb = traceback.format_exc()
            print(f"Full traceback:\n{tb}")  
            # Extract line info properly
            if e.__traceback__:
                tb_lines = traceback.extract_tb(e.__traceback__)
                if tb_lines:
                    last_line = tb_lines[-1]
                    print(f"Failing line number: {last_line.lineno}")
                    print(f"Error type: {type(e).__name__}") 
                    print(f"Error message: {str(e)}")
            else:
                print("Could not extract traceback info")
        else:
            # If no exception was raised, we still want to show the paths
            pass
        
        # Print save path and read path (even if there's no exception)
        print(f"Save path: {scenes_md_path}")
        print(f"Read path: {scenes_md_path}")
        
        # Check if file was written - even without exception handling, let's check this explicitly now
        try:
            if os.path.exists(scenes_md_path):
                print("✓ scenes.md file exists after save")
                
                # Read back the content to verify (this is where real exceptions might occur)
                with open(scenes_md_path, 'r', encoding='utf-8') as f:
                    read_content = f.read()
                print(f"Content read back: {repr(read_content)}")
                
                if read_content == test_content:
                    print("✓ Content matches what was written")
                else:
                    print("✗ Content does NOT match!")
            else:
                print("✗ scenes.md file does NOT exist after save")
        except Exception as e:
            # This is where we'd normally see an exception during reading
            print(f"Error reading file (this should be our target): {e}")  
            tb = traceback.format_exc()
            print(f"Full traceback:\n{tb}") 
            if e.__traceback__:
                tb_lines = traceback.extract_tb(e.__traceback__)
                if tb_lines:
                    last_line = tb_lines[-1]
                    print(f"Failing line number: {last_line.lineno}")
                    print(f"Error type: {type(e).__name__}") 
                    print(f"Error message: {str(e)}")
            else:
                print("Could not extract traceback info")

    except Exception as e:
        # This is our main target - we want to capture this
        print(f"Error in test (this should be our target): {e}")
        import traceback
        tb = traceback.format_exc()
        print(f"Full traceback:\n{tb}")
        if e.__traceback__:
            tb_lines = traceback.extract_tb(e.__traceback__)
            if tb_lines:
                last_line = tb_lines[-1]
                print(f"Failing line number: {last_line.lineno}") 
                print(f"Error type: {type(e).__name__}")
                print(f"Error message: {str(e)}")
        else:
            print("Could not extract traceback info")

except ImportError as e:
    print(f"Import error: {e}")
except Exception as e:
    print(f"General error: {e}")  
    import traceback
    traceback.print_exc()
