"""
AI Studio shared constants.

This module is the single source of truth for application-wide constants.
"""

from __future__ import annotations

from pathlib import Path

# -----------------------------------------------------------------------------
# Application
# -----------------------------------------------------------------------------

APP_NAME = "AI Studio"

APP_VERSION = "0.2.0"

# -----------------------------------------------------------------------------
# Directories
# -----------------------------------------------------------------------------

ROOT_DIRECTORY = Path(__file__).resolve().parents[2]

WORKSPACE_DIRECTORY = ROOT_DIRECTORY / "workspace"

PROJECTS_DIRECTORY = WORKSPACE_DIRECTORY / "projects"

MODELS_DIRECTORY = WORKSPACE_DIRECTORY / "models"

CACHE_DIRECTORY = WORKSPACE_DIRECTORY / "cache"

LOG_DIRECTORY = WORKSPACE_DIRECTORY / "logs"

EXPORT_DIRECTORY = WORKSPACE_DIRECTORY / "exports"

TEMP_DIRECTORY = WORKSPACE_DIRECTORY / "temp"

# -----------------------------------------------------------------------------
# Supported formats
# -----------------------------------------------------------------------------

IMAGE_EXTENSIONS = (
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
)

VIDEO_EXTENSIONS = (
    ".mp4",
    ".mkv",
    ".mov",
)

AUDIO_EXTENSIONS = (
    ".wav",
    ".mp3",
    ".flac",
)

# -----------------------------------------------------------------------------
# Status
# -----------------------------------------------------------------------------

SERVICE_STOPPED = "STOPPED"

SERVICE_STARTING = "STARTING"

SERVICE_RUNNING = "RUNNING"

SERVICE_STOPPING = "STOPPING"

SERVICE_ERROR = "ERROR"