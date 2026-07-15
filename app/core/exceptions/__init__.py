"""
Application exception hierarchy.
"""

from __future__ import annotations


class AIStudioError(Exception):
    """Base application exception."""


class ConfigurationError(AIStudioError):
    """Raised when configuration cannot be loaded."""


class WorkspaceError(AIStudioError):
    """Raised for workspace-related failures."""


class ValidationError(AIStudioError):
    """Raised when validation fails."""


class ServiceError(AIStudioError):
    """Raised by service components."""


__all__ = [
    "AIStudioError",
    "ConfigurationError",
    "WorkspaceError",
    "ValidationError",
    "ServiceError",
]