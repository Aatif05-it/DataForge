"""
Salary Provider

Generate realistic salaries.
"""

from __future__ import annotations

import random

from .base import BaseProvider


class SalaryProvider(BaseProvider):
    """
    Salary generator.

    Example
    -------
    provider = SalaryProvider()

    provider.generate()
    """

    name = "salary"

    def __init__(
        self,
        minimum: int = 25000,
        maximum: int = 200000,
        currency: str = "$",
    ):
        self.minimum = minimum
        self.maximum = maximum
        self.currency = currency

    def generate(self) -> int:
        """
        Generate salary as integer.
        """
        return random.randint(self.minimum, self.maximum)

    def formatted(self) -> str:
        """
        Generate formatted salary.
        """
        return f"{self.currency}{self.generate():,}"

    def monthly(self) -> float:
        """
        Monthly salary.
        """
        return round(self.generate() / 12, 2)

    def weekly(self) -> float:
        """
        Weekly salary.
        """
        return round(self.generate() / 52, 2)

    def daily(self) -> float:
        """
        Daily salary.
        """
        return round(self.generate() / 365, 2)

    def yearly(self) -> int:
        """
        Annual salary.
        """
        return self.generate()

    def custom(
        self,
        minimum: int,
        maximum: int,
    ) -> int:
        """
        Generate salary within custom range.
        """
        return random.randint(minimum, maximum)

    def profile(self) -> dict:
        """
        Complete salary profile.
        """
        salary = self.generate()

        return {
            "salary": salary,
            "formatted": f"{self.currency}{salary:,}",
            "monthly": round(salary / 12, 2),
            "weekly": round(salary / 52, 2),
            "daily": round(salary / 365, 2),
        }