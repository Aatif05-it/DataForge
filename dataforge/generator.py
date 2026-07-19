"""
DataForge Generator Engine

This module contains the core generation engine responsible for
creating synthetic datasets using registered providers.
"""

from __future__ import annotations

from typing import Dict, List, Any

from .providers.name import NameProvider
from .providers.email import EmailProvider
from .providers.phone import PhoneProvider
from .providers.address import AddressProvider
from .providers.salary import SalaryProvider
from .providers.company import CompanyProvider
from .providers.uuid import UUIDProvider
from .providers.password import PasswordProvider


class DataGenerator:
    """
    Core engine that generates rows based on a schema.

    Example
    -------
    schema = {
        "name": "name",
        "email": "email",
        "salary": "salary"
    }

    generator = DataGenerator(schema)

    data = generator.generate(100)
    """

    def __init__(self, schema: Dict[str, str]):

        self.schema = schema

        self.providers = {
            "name": NameProvider(),
            "email": EmailProvider(),
            "phone": PhoneProvider(),
            "address": AddressProvider(),
            "salary": SalaryProvider(),
            "company": CompanyProvider(),
            "uuid": UUIDProvider(),
            "password": PasswordProvider(),
        }

    def generate(self, rows: int) -> List[Dict[str, Any]]:
        """
        Generate dataset.

        Parameters
        ----------
        rows : int

        Returns
        -------
        list[dict]
        """

        dataset = []

        for _ in range(rows):

            row = {}

            for column, provider_name in self.schema.items():

                provider = self.providers.get(provider_name)

                if provider is None:
                    raise ValueError(
                        f"Unknown provider '{provider_name}'."
                    )

                row[column] = provider.generate()

            dataset.append(row)

        return dataset

    def register_provider(
        self,
        name: str,
        provider
    ) -> None:
        """
        Register custom provider.

        Example
        -------

        generator.register_provider(
            "temperature",
            TemperatureProvider()
        )
        """

        self.providers[name] = provider

    def available_providers(self):

        """
        Return available provider names.
        """

        return sorted(self.providers.keys())