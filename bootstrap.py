"""
AI Studio bootstrap entry point.
"""

from __future__ import annotations

import sys

from app.core.version import APP_NAME, VERSION


def bootstrap() -> int:
    """
    Perform early application initialization.
    """

    print(f"{APP_NAME} {VERSION.full}")
    print("Bootstrapping application...")

    return 0


def main() -> int:
    return bootstrap()


if __name__ == "__main__":
    sys.exit(main())