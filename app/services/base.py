"""
Base service implementation.

Every long-running service inside AI Studio derives from this class.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from app.core.constants import (
    SERVICE_ERROR,
    SERVICE_RUNNING,
    SERVICE_STARTING,
    SERVICE_STOPPED,
    SERVICE_STOPPING,
)


class BaseService(ABC):
    """
    Base class for all AI Studio services.
    """

    def __init__(self, name: str) -> None:

        self._name = name

        self._status = SERVICE_STOPPED

    @property
    def name(self) -> str:

        return self._name

    @property
    def status(self) -> str:

        return self._status

    @property
    def running(self) -> bool:

        return self._status == SERVICE_RUNNING

    def start(self) -> None:

        if self.running:
            return

        self._status = SERVICE_STARTING

        try:

            self.on_start()

            self._status = SERVICE_RUNNING

        except Exception:

            self._status = SERVICE_ERROR

            raise

    def stop(self) -> None:

        if not self.running:
            return

        self._status = SERVICE_STOPPING

        try:

            self.on_stop()

            self._status = SERVICE_STOPPED

        except Exception:

            self._status = SERVICE_ERROR

            raise

    @abstractmethod
    def on_start(self) -> None:
        """
        Called when the service starts.
        """

    @abstractmethod
    def on_stop(self) -> None:
        """
        Called when the service stops.
        """