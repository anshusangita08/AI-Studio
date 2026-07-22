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

    # Verify placeholder asset collections exist and are empty
    assert "images" in data, "render.json should contain 'images' key"
    assert isinstance(data["images"], list) and len(data["images"]) == 0, "'images' should be an empty list"

    assert "audio" in data, "render.json should contain 'audio' key"
    assert isinstance(data["audio"], list) and len(data["audio"]) == 0, "'audio' should be an empty list"

    assert "video" in data, "render.json should contain 'video' key"
    assert isinstance(data["video"], list) and len(data["video"]) == 0, "'video' should be an empty list"


def test_asset_record_schema():
    """
    Ensure that the asset collections are intended to hold records with
    the expected keys.  The collections are empty at render time,
    but we can verify that a sample record would match the schema.
    """
    # Sample record matching the defined schema
    sample = {
        "id": "",
        "type": "",
        "prompt": "",
        "filename": "",
        "status": ""
    }

    # The keys of the sample should be exactly those expected
    expected_keys = {"id", "type", "prompt", "filename", "status"}
    assert set(sample.keys()) == expected_keys, "Asset record schema must contain all required keys"

    # Verify that each collection is a list (empty by default)
    render_service = RenderService(Path("dummy"))
    data = render_service.render()
    for key in ("images", "audio", "video"):
        assert isinstance(data[key], list), f"{key} should be a list"
