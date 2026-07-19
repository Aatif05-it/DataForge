"""
Password Provider

Generate secure passwords for testing and development.
"""

from __future__ import annotations

import hashlib
import secrets
import string

from .base import BaseProvider


class PasswordProvider(BaseProvider):
    """
    Password generator.

    Example
    -------
    provider = PasswordProvider()

    provider.generate()
    """

    name = "password"

    def __init__(
        self,
        length: int = 12,
        uppercase: bool = True,
        lowercase: bool = True,
        digits: bool = True,
        symbols: bool = True,
    ):

        self.length = max(8, length)

        self.uppercase = uppercase
        self.lowercase = lowercase
        self.digits = digits
        self.symbols = symbols

    def _characters(self) -> str:

        chars = ""

        if self.uppercase:
            chars += string.ascii_uppercase

        if self.lowercase:
            chars += string.ascii_lowercase

        if self.digits:
            chars += string.digits

        if self.symbols:
            chars += "!@#$%^&*()-_=+?"

        if not chars:
            raise ValueError("No character set selected.")

        return chars

    def generate(self) -> str:
        """
        Generate secure password.
        """

        chars = self._characters()

        return "".join(
            secrets.choice(chars)
            for _ in range(self.length)
        )

    def hash_sha256(self, password: str) -> str:
        """
        SHA256 hash.
        """

        return hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

    def strength(self, password: str) -> str:
        """
        Estimate password strength.
        """

        score = 0

        if len(password) >= 8:
            score += 1

        if any(c.isupper() for c in password):
            score += 1

        if any(c.islower() for c in password):
            score += 1

        if any(c.isdigit() for c in password):
            score += 1

        if any(c in "!@#$%^&*()-_=+?" for c in password):
            score += 1

        if score <= 2:
            return "Weak"

        if score == 3:
            return "Medium"

        if score == 4:
            return "Strong"

        return "Very Strong"

    def profile(self) -> dict:
        """
        Complete password profile.
        """

        password = self.generate()

        return {
            "password": password,
            "length": len(password),
            "strength": self.strength(password),
            "sha256": self.hash_sha256(password),
        }