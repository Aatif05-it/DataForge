"""
DataForge Randomizer

Utility functions for generating random values.
"""

from __future__ import annotations

import random
import string
from typing import Any, Sequence


class Randomizer:
    """
    Utility class for random operations.
    """

    @staticmethod
    def integer(minimum: int = 0, maximum: int = 100) -> int:
        """Generate random integer."""
        return random.randint(minimum, maximum)

    @staticmethod
    def floating(minimum: float = 0.0, maximum: float = 100.0, digits: int = 2) -> float:
        """Generate random float."""
        return round(random.uniform(minimum, maximum), digits)

    @staticmethod
    def boolean() -> bool:
        """Generate random boolean."""
        return random.choice([True, False])

    @staticmethod
    def choice(values: Sequence[Any]) -> Any:
        """Choose random item."""
        return random.choice(values)

    @staticmethod
    def sample(values: Sequence[Any], size: int):
        """Random sample."""
        return random.sample(values, size)

    @staticmethod
    def string(length: int = 10) -> str:
        """Random string."""
        chars = string.ascii_letters
        return "".join(random.choice(chars) for _ in range(length))

    @staticmethod
    def alphanumeric(length: int = 12) -> str:
        """Random alphanumeric string."""
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(length))

    @staticmethod
    def digits(length: int = 6) -> str:
        """Random numeric string."""
        return "".join(random.choice(string.digits) for _ in range(length))

    @staticmethod
    def shuffle(values: list):
        """Shuffle list."""
        random.shuffle(values)
        return values

    @staticmethod
    def seed(seed: int):
        """Set random seed."""
        random.seed(seed)