"""
Email Provider

Generate realistic email addresses.
"""

from __future__ import annotations

from faker import Faker

from .base import BaseProvider


class EmailProvider(BaseProvider):
    """
    Email generator.

    Example
    -------
    provider = EmailProvider()

    provider.generate()
    """

    name = "email"

    def __init__(self, locale: str = "en_US"):

        self.locale = locale
        self.fake = Faker(locale)

    def generate(self) -> str:
        """
        Default email.
        """

        return self.fake.email()

    def company_email(self) -> str:
        """
        Company email.
        """

        return self.fake.company_email()

    def free_email(self) -> str:
        """
        Gmail/Yahoo/Hotmail style email.
        """

        return self.fake.free_email()

    def safe_email(self) -> str:
        """
        Safe email for examples.
        """

        return self.fake.safe_email()

    def ascii_email(self) -> str:
        """
        ASCII email.
        """

        return self.fake.ascii_email()

    def domain(self) -> str:
        """
        Domain name.
        """

        return self.fake.domain_name()

    def username(self) -> str:
        """
        Username only.
        """

        return self.fake.user_name()

    def profile(self) -> dict:
        """
        Email profile.
        """

        return {
            "email": self.generate(),
            "company_email": self.company_email(),
            "free_email": self.free_email(),
            "safe_email": self.safe_email(),
            "domain": self.domain(),
            "username": self.username(),
        }