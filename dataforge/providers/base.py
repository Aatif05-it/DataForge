"""
Base Provider

All providers must inherit from BaseProvider.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Base class for all providers.
    """

    name: str = "base"

    @abstractmethod
    def generate(self):
        """
        Generate one value.
        """
        raise NotImplementedError

    def __call__(self):
        """
        Allow provider()
        """
        return self.generate()

    def __repr__(self):
        return f"<{self.__class__.__name__}>"