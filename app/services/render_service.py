import json
from datetime import datetime, timezone
from pathlib import Path

class RenderService:
    """
    Service responsible for rendering a project.
    It creates a `render/` directory inside the given project root and writes a
    `render.json` file with status information.
    """

    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root

    def render(self) -> dict:
        """
        Create the render folder and write the render.json file.

        Returns:
            The dictionary that was written to `render.json`.
        """
        # Ensure the render directory exists
        render_dir = self.project_root / "render"
        render_dir.mkdir(parents=True, exist_ok=True)

        # Prepare the data to be written
        data = {
            "status": "completed",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        # Write JSON file
        json_path = render_dir / "render.json"
        with json_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return data
