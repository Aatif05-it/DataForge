"""
DataForge Configuration
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Config:
    """
    Global configuration.
    """

    DEFAULT_ROWS: int = 100

    DEFAULT_LOCALE: str = "en_US"

    RANDOM_SEED: int | None = None

    CSV_ENCODING: str = "utf-8"

    EXCEL_SHEET: str = "Sheet1"

    SQLITE_TABLE: str = "data"

    EXPORT_INDEX: bool = False

    JSON_INDENT: int = 4

    VERSION: str = "0.1.0"

    AUTHOR: str = "Your Name"

    LICENSE: str = "MIT"


config = Config()