"""
Company Provider

Generate realistic company information.
"""

from __future__ import annotations

from faker import Faker

from .base import BaseProvider


class CompanyProvider(BaseProvider):
    """
    Company generator.

    Example
    -------
    provider = CompanyProvider()

    provider.generate()
    """

    name = "company"

    def __init__(self, locale: str = "en_US"):

        self.locale = locale
        self.fake = Faker(locale)

    def generate(self) -> str:
        """
        Company name.
        """
        return self.fake.company()

    def company_suffix(self) -> str:
        """
        Company suffix.
        """
        return self.fake.company_suffix()

    def catch_phrase(self) -> str:
        """
        Company catch phrase.
        """
        return self.fake.catch_phrase()

    def job(self) -> str:
        """
        Random job title.
        """
        return self.fake.job()

    def department(self) -> str:
        """
        Random department.
        """
        departments = [
            "Engineering",
            "Finance",
            "Marketing",
            "Human Resources",
            "Operations",
            "Sales",
            "Research",
            "Customer Support",
            "IT",
            "Administration",
        ]

        return self.fake.random_element(departments)

    def industry(self) -> str:
        """
        Random industry.
        """
        industries = [
            "Technology",
            "Healthcare",
            "Education",
            "Manufacturing",
            "Retail",
            "Finance",
            "Agriculture",
            "Transportation",
            "Construction",
            "Telecommunications",
            "Entertainment",
            "Energy",
        ]

        return self.fake.random_element(industries)

    def website(self) -> str:
        """
        Company website.
        """
        return self.fake.url()

    def profile(self) -> dict:
        """
        Complete company profile.
        """

        return {
            "company": self.generate(),
            "industry": self.industry(),
            "department": self.department(),
            "job": self.job(),
            "website": self.website(),
            "catch_phrase": self.catch_phrase(),
            "suffix": self.company_suffix(),
        }