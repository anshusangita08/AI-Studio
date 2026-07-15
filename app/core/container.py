"""
Simple dependency injection container.
"""

from __future__ import annotations

from typing import Any


class Container:
    """
    Central registry for application singletons.
    """

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        if name in self._services:
            raise ValueError(f"Service '{name}' already registered.")

        self._services[name] = service

    def resolve(self, name: str) -> Any:
        try:
            return self._services[name]
        except KeyError as exc:
            raise KeyError(f"Unknown service '{name}'.") from exc

    def exists(self, name: str) -> bool:
        return name in self._services

    def clear(self) -> None:
        self._services.clear()


container = Container()