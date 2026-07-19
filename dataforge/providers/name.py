"""
Name Provider

Generates realistic person names.
"""

from __future__ import annotations

from faker import Faker

from .base import BaseProvider


class NameProvider(BaseProvider):
    """
    Generate fake names.

    Example
    -------
    provider = NameProvider()

    provider.generate()

    'John Smith'
    """

    name = "name"

    def __init__(self, locale: str = "en_US"):

        self.locale = locale
        self.fake = Faker(locale)

    def generate(self) -> str:
        """
        Return a full name.
        """

        return self.fake.name()

    def first_name(self) -> str:
        """
        Generate first name.
        """

        return self.fake.first_name()

    def last_name(self) -> str:
        """
        Generate last name.
        """

        return self.fake.last_name()

    def prefix(self) -> str:
        """
        Generate name prefix.
        """

        return self.fake.prefix()

    def suffix(self) -> str:
        """
        Generate suffix.
        """

        return self.fake.suffix()

    def profile(self) -> dict:
        """
        Return complete profile.
        """

        return {
            "first_name": self.first_name(),
            "last_name": self.last_name(),
            "full_name": self.generate(),
            "prefix": self.prefix(),
            "suffix": self.suffix(),
        }