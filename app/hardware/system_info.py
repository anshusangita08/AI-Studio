"""
System information utilities.
"""

from __future__ import annotations

import platform
import shutil
from dataclasses import dataclass

import psutil


@dataclass(slots=True, frozen=True)
class SystemInfo:
    operating_system: str
    python_version: str
    cpu: str
    logical_cores: int
    ram_gb: float
    ffmpeg_available: bool
    ollama_available: bool


def get_system_info() -> SystemInfo:
    return SystemInfo(
        operating_system=f"{platform.system()} {platform.release()}",
        python_version=platform.python_version(),
        cpu=platform.processor(),
        logical_cores=psutil.cpu_count(logical=True) or 0,
        ram_gb=round(psutil.virtual_memory().total / 1024**3, 2),
        ffmpeg_available=shutil.which("ffmpeg") is not None,
        ollama_available=shutil.which("ollama") is not None,
    )