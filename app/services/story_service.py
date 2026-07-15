"""
Story management service.
"""

from __future__ import annotations

from pathlib import Path


class StoryService:
    """
    Handles reading and writing project stories.
    """

    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root

    def story_file(
        self,
        slug: str,
    ) -> Path:

        return (
            self.project_root
            / slug
            / "story"
            / "story.md"
        )

    def load(
        self,
        slug: str,
    ) -> str:

        story = self.story_file(slug)

        if not story.exists():
            return ""

        return story.read_text(
            encoding="utf-8",
        )

    def save(
        self,
        slug: str,
        content: str,
    ) -> None:

        story = self.story_file(slug)

        story.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        story.write_text(
            content,
            encoding="utf-8",
        )