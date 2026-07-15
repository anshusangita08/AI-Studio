"""
Application bootstrap.

Responsible for initializing every core subsystem before the web server starts.
"""

from __future__ import annotations

from app.core.config import config
from app.core.logging import logger
from app.core.workspace import workspace
from app.hardware.requirements import validate_environment


class Bootstrap:
    """Application bootstrap manager."""

    def initialize(self) -> None:
        """Initialize all core subsystems."""

        workspace.initialize()

        config.load()

        validate_environment()

        logger.info("Workspace initialized")
        logger.info("Configuration loaded")
        logger.info("Environment validated")
        logger.info("Bootstrap complete")


bootstrap = Bootstrap()