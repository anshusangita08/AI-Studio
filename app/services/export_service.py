"""
Export service.
"""

import json
import zipfile
from datetime import UTC, datetime
from pathlib import Path
import os

class ExportService:
    """
    Handles creation of export ZIPs for projects.
    """

    EXCLUDE_DIRS = {"cache", "temp", "exports"}

    def __init__(self, root: Path) -> None:
        self.root = root

    def create_export(self, slug: str, pipeline_status: dict) -> Path:
        """
        Create a ZIP archive containing the project's exportable data.

        Returns the path to the created ZIP file.
        """
        project_dir = self.root / slug
        if not project_dir.exists():
            raise FileNotFoundError(f"Project '{slug}' does not exist")

        # Determine output directory and filename
        exports_dir = project_dir / "exports"
        exports_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
        zip_name = f"{slug}-{timestamp}.zip"
        zip_path = exports_dir / zip_name

        # Walk the project directory and include everything except excluded dirs
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(project_dir):
                # Skip excluded directories
                dirs[:] = [d for d in dirs if d not in self.EXCLUDE_DIRS]
                for file_name in files:
                    file_path = Path(root) / file_name
                    arcname = str(file_path.relative_to(project_dir))
                    zf.write(file_path, arcname=arcname)

            # Add manifest.json with provided pipeline status and milestone
            manifest: dict = {
                "timestamp": timestamp,
                "project_slug": slug,
                "pipeline_status": pipeline_status,
                "milestone": "011",
            }
            zf.writestr("manifest.json", json.dumps(manifest, indent=2))

        return zip_path
