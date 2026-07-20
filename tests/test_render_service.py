import os
import shutil
from pathlib import Path

import pytest

from app.services.render_service import RenderService


@pytest.fixture
def temp_project(tmp_path: Path) -> Path:
    """
    Create a temporary project directory for testing.
    """
    # Mimic the structure expected by other services if needed
    (tmp_path / "project").mkdir()
    return tmp_path


def test_render_creates_directory_and_file(temp_project):
    render_service = RenderService(temp_project)
    result = render_service.render()

    # Check that the directory was created
    render_dir = temp_project / "render"
    assert render_dir.is_dir(), "Render directory should exist"

    # Check that the JSON file exists
    json_path = render_dir / "render.json"
    assert json_path.is_file(), "render.json should be created"

    # Verify contents of the JSON file
    with json_path.open("r", encoding="utf-8") as f:
        import json

        data = json.load(f)

    assert data == result, "Returned dict should match written JSON"
    assert data["status"] == "completed", "Status should be 'completed'"
    # Ensure timestamp is a valid ISO8601 string
    from datetime import datetime

    try:
        parsed_ts = datetime.fromisoformat(data["timestamp"])
    except ValueError:
        pytest.fail("Timestamp is not a valid ISO8601 string")
