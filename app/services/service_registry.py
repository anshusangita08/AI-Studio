"""
Service registry.

Tracks application services.
"""

from __future__ import annotations


class ServiceRegistry:
    def __init__(self) -> None:
        self._services: dict[str, object] = {}

    def register(self, name: str, service: object) -> None:
        self._services[name] = service

    def get(self, name: str) -> object:
        return self._services[name]

    def names(self) -> list[str]:
        return sorted(self._services.keys())


services = ServiceRegistry()