#!/usr/bin/env python3

import sys
sys.path.insert(0, '.')

# Import and immediately check PROJECT_ROOT location 
from app.services.project_service import PROJECT_ROOT, project_service
print('=== BEFORE TEST EXECUTION ===')
print(f'PROJECT_ROOT = {PROJECT_ROOT}')
print(f'project_service = {project_service}')

# Look at the test function to see how it's structured  
import inspect
from tests.test_project_service import test_create_reserved_project_name

# Check what globals are available in the test function context
test_source = inspect.getsource(test_create_reserved_project_name)
print('=== TEST FUNCTION SOURCE ===')
print(test_source[:500] + '...')  # First 500 chars

# Let's also look at how project_service is imported in tests  
test_imports = '''
from app.services.project_service import (
    PROJECT_ROOT,
    project_service,
)
'''
print('=== IMPORTS IN TEST ===')
print(test_imports)

# Now run a minimal version of the test to see what happens
print('\n=== SIMULATING THE TEST ===')

import tempfile
import shutil

def cleanup_all_projects():
    """Remove all projects to avoid conflicts in tests."""
    import glob
    # Remove all project directories except the one we know exists  
    for project_dir in PROJECT_ROOT.iterdir():
        if project_dir.is_dir() and not (project_dir / "project.json").exists():
            continue  # Skip non-project directories
        try:
            shutil.rmtree(project_dir)
        except Exception:
            pass  # Continue even if some cleanup fails

# Execute the actual test logic step by step to see PROJECT_ROOT value  
print(f'Before cleanup_all_projects(): PROJECT_ROOT = {PROJECT_ROOT}')

# This is what happens in the test
cleanup_all_projects()
print('After cleanup_all_projects(): PROJECT_ROOT still =', PROJECT_ROOT)

# Test creating a valid project (this creates folders)
try:
    result = project_service.create("Valid Project Name")
    print(f'Successfully created: "{result.name}" with slug "{result.slug}"')
    print(f'Folder was created at: {PROJECT_ROOT / result.slug}')
    
    # Show what directories were created
    project_folder = PROJECT_ROOT / result.slug
    if project_folder.exists():
        print('Created subdirectories:')
        for item in project_folder.iterdir():
            if item.is_dir():
                print(f'  {item.name}')
                
except Exception as e:
    print(f'Error: {e}')

# Clean up 
if (PROJECT_ROOT / "valid-project-name").exists():
    shutil.rmtree(PROJECT_ROOT / "valid-project-name")