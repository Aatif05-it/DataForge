"""
Helper Utilities
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime


def ensure_directory(path: str | Path) -> Path:
    """
    Create directory if it does not exist.
    """
    path = Path(path)

    path.mkdir(parents=True, exist_ok=True)

    return path


def file_exists(path: str | Path) -> bool:
    """
    Check if file exists.
    """
    return Path(path).exists()


def timestamp() -> str:
    """
    Current timestamp.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def filename_without_extension(path: str | Path) -> str:
    """
    File name only.
    """
    return Path(path).stem


def extension(path: str | Path) -> str:
    """
    File extension.
    """
    return Path(path).suffix


def bytes_to_mb(size: int) -> float:
    """
    Convert bytes to MB.
    """
    return round(size / (1024 * 1024), 2)


def is_positive(number: int | float) -> bool:
    """
    Check positive number.
    """
    return number > 0


def is_empty(value) -> bool:
    """
    Check empty value.
    """
    return value is None or value == ""


def flatten(items):
    """
    Flatten nested list.
    """
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


def chunks(items, size):
    """
    Split list into chunks.
    """
    for i in range(0, len(items), size):
        yield items[i:i + size]