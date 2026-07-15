"""
Project domain model.

Represents an AI Studio project and its on-disk layout.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
import json
import uuid


@dataclass(slots=True)
class Project:
    id: str
    name: str
    slug: str
    created_at: str
    updated_at: str

    @classmethod
    def create(cls, name: str) -> "Project":
        now = datetime.now(UTC).isoformat(timespec="seconds")

        slug = (
            name.strip()
            .lower()
            .replace(" ", "-")
            .replace("_", "-")
        )

        return cls(
            id=str(uuid.uuid4()),
            name=name.strip(),
            slug=slug,
            created_at=now,
            updated_at=now,
        )

    def to_dict(self) -> dict:
        return asdict(self)

    def save(self, folder: Path) -> None:
        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        with (folder / "project.json").open(
            "w",
            encoding="utf-8",
        ) as fp:
            json.dump(
                self.to_dict(),
                fp,
                indent=4,
            )