"""
Address Provider

Generate realistic addresses.
"""

from __future__ import annotations

from faker import Faker

from .base import BaseProvider


class AddressProvider(BaseProvider):
    """
    Address generator.

    Example
    -------
    provider = AddressProvider()

    provider.generate()
    """

    name = "address"

    def __init__(self, locale: str = "en_US"):

        self.locale = locale
        self.fake = Faker(locale)

    def generate(self) -> str:
        """
        Full address.
        """
        return self.fake.address().replace("\n", ", ")

    def street(self) -> str:
        """
        Street address.
        """
        return self.fake.street_address()

    def city(self) -> str:
        """
        City name.
        """
        return self.fake.city()

    def state(self) -> str:
        """
        State name.
        """
        return self.fake.state()

    def country(self) -> str:
        """
        Country name.
        """
        return self.fake.country()

    def postcode(self) -> str:
        """
        Postal code.
        """
        return self.fake.postcode()

    def latitude(self) -> float:
        """
        Latitude.
        """
        return float(self.fake.latitude())

    def longitude(self) -> float:
        """
        Longitude.
        """
        return float(self.fake.longitude())

    def coordinates(self) -> dict:
        """
        Latitude and longitude.
        """
        return {
            "latitude": self.latitude(),
            "longitude": self.longitude(),
        }

    def profile(self) -> dict:
        """
        Complete address profile.
        """
        return {
            "address": self.generate(),
            "street": self.street(),
            "city": self.city(),
            "state": self.state(),
            "country": self.country(),
            "postcode": self.postcode(),
            "coordinates": self.coordinates(),
        }