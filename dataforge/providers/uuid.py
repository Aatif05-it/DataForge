"""
UUID Provider

Generate UUIDs for unique identifiers.
"""

from __future__ import annotations

import uuid

from .base import BaseProvider


class UUIDProvider(BaseProvider):
    """
    UUID generator.

    Example
    -------
    provider = UUIDProvider()

    provider.generate()
    """

    name = "uuid"

    def generate(self) -> str:
        """
        Generate UUID version 4.
        """
        return str(uuid.uuid4())

    def uuid1(self) -> str:
        """
        Generate UUID version 1.
        """
        return str(uuid.uuid1())

    def uuid3(self, namespace: uuid.UUID = uuid.NAMESPACE_DNS, name: str = "dataforge") -> str:
        """
        Generate UUID version 3.
        """
        return str(uuid.uuid3(namespace, name))

    def uuid5(self, namespace: uuid.UUID = uuid.NAMESPACE_DNS, name: str = "dataforge") -> str:
        """
        Generate UUID version 5.
        """
        return str(uuid.uuid5(namespace, name))

    def hex(self) -> str:
        """
        UUID as hexadecimal string.
        """
        return uuid.uuid4().hex

    def integer(self) -> int:
        """
        UUID as integer.
        """
        return uuid.uuid4().int

    def bytes(self) -> bytes:
        """
        UUID as bytes.
        """
        return uuid.uuid4().bytes

    def urn(self) -> str:
        """
        UUID as URN.
        """
        return uuid.uuid4().urn

    def profile(self) -> dict:
        """
        Complete UUID profile.
        """
        u = uuid.uuid4()

        return {
            "uuid": str(u),
            "hex": u.hex,
            "int": u.int,
            "urn": u.urn,
            "version": u.version,
            "variant": str(u.variant),
        }