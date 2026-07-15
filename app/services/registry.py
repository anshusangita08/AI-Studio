"""
Service registry.
"""

from __future__ import annotations

from app.services.base import BaseService


class ServiceRegistry:
    """
    Stores every application service.
    """

    def __init__(self) -> None:
        self._services: dict[str, BaseService] = {}

    def register(self, service: BaseService) -> None:
        if service.name in self._services:
            raise ValueError(
                f"Service '{service.name}' already registered."
            )

        self._services[service.name] = service

    def get(self, name: str) -> BaseService:
        return self._services[name]

    def start_all(self) -> None:
        for service in self._services.values():
            service.start()

    def stop_all(self) -> None:
        for service in reversed(list(self._services.values())):
            service.stop()

    def names(self) -> list[str]:
        return sorted(self._services.keys())

    def count(self) -> int:
        return len(self._services)


registry = ServiceRegistry()