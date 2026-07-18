#!/usr/bin/env python3

import sys
sys.path.insert(0, '.')

# Check PROJECT_ROOT value
from app.services.project_service import PROJECT_ROOT, project_service

print('PROJECT_ROOT at runtime:', PROJECT_ROOT)
print('project_service type:', type(project_service))
print('project_service.__class__:', project_service.__class__)
print('project_service.__class__.__dict__.keys():', list(project_service.__class__.__dict__.keys()))

# Let's also check the class definition more carefully
import inspect
source = inspect.getsource(project_service.__class__)
print('ProjectService class source (first few lines):')
lines = source.split('\n')
for i, line in enumerate(lines[:20]):
    print(f'{i+1:2}: {line}')