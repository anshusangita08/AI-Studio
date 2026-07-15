"""
Configuration loader.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from app.core.exceptions import ConfigurationError

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONFIG = ROOT / "config" / "default.json"


class Config:
    """
    Read-only application configuration.
    """

    def __init__(self, path: Path | None = None) -> None:
        self._path = path or DEFAULT_CONFIG
        self._data: dict[str, Any] = {}

    def load(self) -> None:
        if not self._path.exists():
            raise ConfigurationError(
                f"Configuration file not found: {self._path}"
            )

        try:
            with self._path.open(
                "r",
                encoding="utf-8",
            ) as fp:
                content = fp.read().strip()

            if not content:
                raise ConfigurationError(
                    f"Configuration file is empty: {self._path}"
                )

            self._data = json.loads(content)

        except json.JSONDecodeError as exc:
            raise ConfigurationError(
                f"Invalid JSON in configuration file: {self._path}"
            ) from exc

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    @property
    def data(self) -> dict[str, Any]:
        return dict(self._data)


config = Config()

__all__ = [
    "Config",
    "config",
]