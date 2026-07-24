"""
AI Studio - Repository Dump Utility
===================================

Purpose
-------
Generate a clean repository dump for code reviews.

Run
---
    python tools/dump_repository.py

Output
------
review/
├── directory_tree.txt
├── file_list.txt
└── repository_dump.txt

Notes
-----
- Overwrites existing output files.
- Excludes caches, temporary files and tool-specific folders.
- Produces deterministic (sorted) output.
"""

from pathlib import Path
import shutil

# ============================================================================
# Configuration
# ============================================================================

# Repository root (script is located in tools/)
REPO_ROOT = Path(__file__).resolve().parent.parent

# Output directory
OUTPUT_DIR = REPO_ROOT / "review"

# Output files
TREE_FILE = OUTPUT_DIR / "directory_tree.txt"
FILE_LIST_FILE = OUTPUT_DIR / "file_list.txt"
DUMP_FILE = OUTPUT_DIR / "repository_dump.txt"

# Directories to completely ignore
EXCLUDED_DIRS = {
    ".git",
    ".github",
    ".idea",
    ".vscode",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".continue",
    ".aider.tags.cache.v4",
    "review",
    "docs/old",
    "workspace/logs",
    "workspace/temp",
    "workspace/models",
    "workspace/downloads",
}

# Files to ignore
EXCLUDED_FILES = {
    "package-lock.json",
    "AI-Studio.zip",
    ".aider.chat.history.md",
    ".aider.input.history",
    ".env",
}

# File extensions to include in repository dump
INCLUDED_EXTENSIONS = {
    ".py",
    ".html",
    ".css",
    ".js",
    ".json",
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".toml",
    ".bat",
}


# ============================================================================
# Helper Functions
# ============================================================================

def is_excluded(path: Path) -> bool:
    """
    Returns True if a file or directory should be excluded.
    """

    relative = path.relative_to(REPO_ROOT).as_posix()

    if path.name in EXCLUDED_FILES:
        return True

    for excluded in EXCLUDED_DIRS:
        excluded = excluded.replace("\\", "/")

        if relative == excluded:
            return True

        if relative.startswith(excluded + "/"):
            return True

    return False


def build_directory_tree() -> list[str]:
    """
    Build a simple sorted directory tree.
    """

    lines = []

    directories = sorted(
        [
            p.relative_to(REPO_ROOT).as_posix()
            for p in REPO_ROOT.rglob("*")
            if p.is_dir() and not is_excluded(p)
        ]
    )

    for directory in directories:
        lines.append(directory)

    return lines


def build_file_list() -> list[Path]:
    """
    Build a sorted list of included files.
    """

    files = []

    for path in REPO_ROOT.rglob("*"):

        if not path.is_file():
            continue

        if is_excluded(path):
            continue

        if path.suffix.lower() not in INCLUDED_EXTENSIONS:
            continue

        files.append(path)

    return sorted(files)


def write_repository_dump(files: list[Path]) -> None:
    """
    Write all source files into a single review document.
    """

    separator = "=" * 100

    with DUMP_FILE.open("w", encoding="utf-8") as output:

        for file in files:

            relative = file.relative_to(REPO_ROOT).as_posix()

            output.write(f"{separator}\n")
            output.write(f"FILE: {relative}\n")
            output.write(f"{separator}\n\n")

            try:
                output.write(file.read_text(encoding="utf-8"))
            except UnicodeDecodeError:
                output.write(
                    file.read_text(
                        encoding="utf-8",
                        errors="replace",
                    )
                )

            output.write("\n\n")


# ============================================================================
# Main
# ============================================================================

def main():

    # Remove previous review output
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    OUTPUT_DIR.mkdir(parents=True)

    directories = build_directory_tree()
    files = build_file_list()

    # Directory tree
    TREE_FILE.write_text(
        "\n".join(directories),
        encoding="utf-8",
    )

    # File list
    FILE_LIST_FILE.write_text(
        "\n".join(
            f.relative_to(REPO_ROOT).as_posix()
            for f in files
        ),
        encoding="utf-8",
    )

    # Repository dump
    write_repository_dump(files)

    print("\nRepository dump complete.\n")
    print(f"Directories : {len(directories)}")
    print(f"Files       : {len(files)}")
    print("\nGenerated:")
    print(f"  {TREE_FILE.relative_to(REPO_ROOT)}")
    print(f"  {FILE_LIST_FILE.relative_to(REPO_ROOT)}")
    print(f"  {DUMP_FILE.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()