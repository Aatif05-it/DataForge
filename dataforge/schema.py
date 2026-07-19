"""
DataForge Schema

Schema validation and parsing.
"""

from __future__ import annotations

from typing import Dict


SUPPORTED_PROVIDERS = {
    "name",
    "email",
    "phone",
    "address",
    "salary",
    "company",
    "uuid",
    "password",
}


class Schema:
    """
    Schema validator.

    Example
    -------
    schema = Schema(
        {
            "name": "name",
            "email": "email"
        }
    )

    schema.validate()
    """

    def __init__(self, schema: Dict[str, str]):

        self.schema = schema

    def validate(self) -> bool:
        """
        Validate schema.
        """

        if not isinstance(self.schema, dict):
            raise TypeError(
                "Schema must be a dictionary."
            )

        if len(self.schema) == 0:
            raise ValueError(
                "Schema cannot be empty."
            )

        for column, provider in self.schema.items():

            if not isinstance(column, str):
                raise TypeError(
                    f"Invalid column name: {column}"
                )

            if not isinstance(provider, str):
                raise TypeError(
                    f"Invalid provider for '{column}'."
                )

            if provider not in SUPPORTED_PROVIDERS:
                raise ValueError(
                    f"Unknown provider '{provider}'. "
                    f"Supported providers are: "
                    f"{', '.join(sorted(SUPPORTED_PROVIDERS))}"
                )

        return True

    def columns(self):
        """
        Return all column names.
        """
        return list(self.schema.keys())

    def providers(self):
        """
        Return all provider names.
        """
        return list(self.schema.values())

    def items(self):
        """
        Return schema items.
        """
        return self.schema.items()

    def size(self):
        """
        Number of columns.
        """
        return len(self.schema)

    def __len__(self):
        return len(self.schema)

    def __iter__(self):
        return iter(self.schema.items())

    def __repr__(self):

        return (
            f"Schema("
            f"columns={len(self.schema)})"
        )