import pytest
from unittest.mock import patch, MagicMock

from app.ui.routes_story import router


@pytest.fixture
def mock_story_service():
    service = MagicMock()
    return service


@pytest.fixture
def mock_project_service():
    service = MagicMock()
    return service


def test_story_route_exists():
    """Test that the story routes are defined"""
    assert router is not None
    # We're just testing that this imports and exists, no deep testing needed here