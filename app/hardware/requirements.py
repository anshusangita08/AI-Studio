"""
Startup validation.
"""

from __future__ import annotations

import sys

from app.hardware.system_info import get_system_info


MIN_PYTHON = (3, 11)


def validate_environment() -> None:
    if sys.version_info < MIN_PYTHON:
        raise RuntimeError(
            f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or newer is required."
        )

    info = get_system_info()

    print(f"CPU : {info.cpu}")
    print(f"RAM : {info.ram_gb} GB")
    print(f"Python : {info.python_version}")
    print(f"FFmpeg : {'YES' if info.ffmpeg_available else 'NO'}")
    print(f"Ollama : {'YES' if info.ollama_available else 'NO'}")