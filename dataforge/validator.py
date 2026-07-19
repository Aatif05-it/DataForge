"""
Validation utilities.
"""

from __future__ import annotations

from typing import Dict

from .exceptions import (
    InvalidRowsError,
    SchemaError,
)

from .schema import SUPPORTED_PROVIDERS


class Validator:
    """
    Validate DataForge input.
    """

    @staticmethod
    def rows(rows: int):

        if not isinstance(rows, int):
            raise InvalidRowsError(
                "Rows must be an integer."
            )

        if rows <= 0:
            raise InvalidRowsError(
                "Rows must be greater than zero."
            )

        return True

    @staticmethod
    def schema(schema: Dict[str, str]):

        if not isinstance(schema, dict):
            raise SchemaError(
                "Schema must be dictionary."
            )

        if len(schema) == 0:
            raise SchemaError(
                "Schema cannot be empty."
            )

        for column, provider in schema.items():

            if not isinstance(column, str):
                raise SchemaError(
                    f"Invalid column '{column}'."
                )

            if provider not in SUPPORTED_PROVIDERS:
                raise SchemaError(
                    f"Unknown provider '{provider}'."
                )

        return True