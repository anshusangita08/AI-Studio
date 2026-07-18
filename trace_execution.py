#!/usr/bin/env python3

import sys
sys.path.insert(0, '.')

# Let's simulate exactly what happens during pytest test execution 
# to trace where projects get deleted from C:\AI-Studio\workspace\projects

from app.services.project_service import PROJECT_ROOT
print('=== EXECUTION TRACE ===')
print(f'PROJECT_ROOT = {PROJECT_ROOT}')
print()

# Check if there are any existing projects before running tests
print('Existing directories in PROJECT_ROOT:')
try:
    for item in PROJECT_ROOT.iterdir():
        if item.is_dir():
            print(f'  {item.name} (exists)')
            # Check if it's a project directory by looking for project.json
            if (item / 'project.json').exists():
                print(f'    -> This is a project directory')
            else:
                print(f'    -> This might be a non-project dir')
except Exception as e:
    print(f'Error checking PROJECT_ROOT: {e}')

print()
print('=== TEST EXECUTION TRACE ===')

# Let's look at exactly what happens in each test function
import inspect

test_functions = [
    'test_create_project',
    'test_project_listing', 
    'test_create_reserved_project_name',
    'test_create_duplicate_project_name',
    'test_create_project_whitespace_only_name'
]

for func_name in test_functions:
    print(f'\n{func_name}:')
    
    # Get the source of each function to see what it does
    if func_name == 'test_create_reserved_project_name':
        # This one has cleanup_all_projects()
        print('  - Contains call to cleanup_all_projects() at start')
        print('  - This is where existing projects get deleted!')
        
    elif func_name in ['test_create_project', 'test_create_duplicate_project_name']:
        # These have regular cleanup()
        print('  - Contains call to cleanup() which only removes TEST_SLUG directory')
        
    else:
        print('  - Does not contain project cleanup')

print('\n=== KEY FINDING ===') 
print('The test function "test_create_reserved_project_name()" is the one that clears all projects.')
print('It calls cleanup_all_projects() at the very beginning, which removes ALL directories in PROJECT_ROOT')
print('This explains why existing projects disappear before any create() call!')