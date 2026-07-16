"""
Service registry.

Tracks application services.
"""

from __future__ import annotations

from collections.abc import Iterator


class ServiceRegistry:
    def __init__(self) -> None:
        self._services: dict[str, object] = {}

    def register(self, name: str, service: object) -> None:
        self._services[name] = service

    def unregister(self, name: str) -> None:
        self._services.pop(name, None)

    def get(self, name: str) -> object:
        return self._services[name]

    def get_optional(self, name: str) -> object | None:
        return self._services.get(name)

    def exists(self, name: str) -> bool:
        return name in self._services

    def clear(self) -> None:
        self._services.clear()

    def names(self) -> list[str]:
        return sorted(self._services.keys())

    def items(self) -> Iterator[tuple[str, object]]:
        return iter(self._services.items())

    def __contains__(self, name: str) -> bool:
        return name in self._services

    def __len__(self) -> int:
        return len(self._services)


services = ServiceRegistry()