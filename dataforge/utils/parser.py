"""
Schema Parser
"""

from __future__ import annotations

from typing import Dict


class SchemaParser:
    """
    Parse schema definitions.
    """

    @staticmethod
    def parse(schema) -> Dict[str, str]:
        """
        Convert schema into dictionary.

        Supports:
        dict

        Future:
        JSON
        YAML
        TOML
        """

        if isinstance(schema, dict):
            return schema

        raise TypeError(
            "Schema must be a dictionary."
        )

    @staticmethod
    def columns(schema: Dict[str, str]):
        """Return column names."""
        return list(schema.keys())

    @staticmethod
    def providers(schema: Dict[str, str]):
        """Return provider names."""
        return list(schema.values())

    @staticmethod
    def size(schema: Dict[str, str]):
        """Number of columns."""
        return len(schema)