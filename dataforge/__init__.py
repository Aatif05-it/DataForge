"""
DataForge
==========

A modern Python library for generating realistic synthetic datasets.

Example
-------
>>> from dataforge import forge
>>>
>>> df = forge(
...     rows=100,
...     schema={
...         "name": "name",
...         "email": "email",
...         "salary": "salary"
...     }
... )

Author: Khan Aatif
License: MIT
"""

from .forge import forge

__version__ = "0.1.0"
__author__ = "Khan Aatif"
__license__ = "MIT"

__all__ = [
    "forge",
]