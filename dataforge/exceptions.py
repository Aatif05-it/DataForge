"""
DataForge Exceptions
"""

from __future__ import annotations


class DataForgeError(Exception):
    """
    Base exception.
    """


class SchemaError(DataForgeError):
    """
    Invalid schema.
    """


class ProviderError(DataForgeError):
    """
    Provider error.
    """


class ExportError(DataForgeError):
    """
    Export failed.
    """


class ValidationError(DataForgeError):
    """
    Validation error.
    """


class ConfigurationError(DataForgeError):
    """
    Configuration error.
    """


class GeneratorError(DataForgeError):
    """
    Generator error.
    """


class UnsupportedProviderError(ProviderError):
    """
    Unknown provider.
    """


class InvalidRowsError(ValidationError):
    """
    Invalid row count.
    """