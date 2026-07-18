"""
Pytest configuration.

Ensures the project root is available on sys.path.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Import pytest to avoid NameError in fixtures later if needed (though we're not using them yet)
try:
    import pytest
except ImportError:
    pass  # This might be fine for basic functionality
ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Create isolated test environment for project tests to avoid writing to real workspace/projects directory
@pytest.fixture(scope="session")
def temp_test_workspace(tmp_path_factory):
    """Create a temporary workspace for all tests that need it."""
    # Create main temp dir for this session's testing
    temp_dir = tmp_path_factory.mktemp("test_workspace") 
    return temp_dir

# This approach won't work directly since we can't easily modify global constants in production code during runtime
# But the cleanest solution is to run tests with isolated environment using PYTHONPATH or environment vars

