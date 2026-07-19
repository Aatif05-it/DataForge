"""
Phone Provider

Generate realistic phone numbers.
"""

from __future__ import annotations

from faker import Faker

from .base import BaseProvider


class PhoneProvider(BaseProvider):
    """
    Phone number generator.

    Example
    -------
    provider = PhoneProvider()

    provider.generate()
    """

    name = "phone"

    def __init__(self, locale: str = "en_US"):

        self.locale = locale
        self.fake = Faker(locale)

    def generate(self) -> str:
        """
        Default phone number.
        """
        return self.fake.phone_number()

    def international(self) -> str:
        """
        International phone number.
        """
        return self.fake.msisdn()

    def country_code(self) -> str:
        """
        Country calling code.
        """
        return self.fake.country_calling_code()

    def profile(self) -> dict:
        """
        Complete phone profile.
        """
        return {
            "phone": self.generate(),
            "international": self.international(),
            "country_code": self.country_code(),
        }