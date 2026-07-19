"""
DataForge Providers

This package contains all built-in data providers.
"""

from .base import BaseProvider
from .name import NameProvider
from .email import EmailProvider
from .phone import PhoneProvider
from .address import AddressProvider
from .salary import SalaryProvider
from .company import CompanyProvider
from .uuid import UUIDProvider
from .password import PasswordProvider

__all__ = [
    "BaseProvider",
    "NameProvider",
    "EmailProvider",
    "PhoneProvider",
    "AddressProvider",
    "SalaryProvider",
    "CompanyProvider",
    "UUIDProvider",
    "PasswordProvider",
]