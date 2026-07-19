"""
DataForge Core API
------------------

Public function:

    forge(rows, schema)

Returns a pandas DataFrame filled with synthetic data.
"""

from __future__ import annotations

from typing import Dict

import pandas as pd

from .generator import DataGenerator


def forge(
    rows: int,
    schema: Dict[str, str],
) -> pd.DataFrame:
    """
    Generate a synthetic dataset.

    Parameters
    ----------
    rows : int
        Number of records.

    schema : dict
        Example

        {
            "name": "name",
            "email": "email",
            "salary": "salary"
        }

    Returns
    -------
    pandas.DataFrame
    """

    if not isinstance(rows, int):
        raise TypeError("rows must be an integer.")

    if rows <= 0:
        raise ValueError("rows must be greater than zero.")

    if not isinstance(schema, dict):
        raise TypeError("schema must be a dictionary.")

    if len(schema) == 0:
        raise ValueError("schema cannot be empty.")

    generator = DataGenerator(schema)

    records = generator.generate(rows)

    return pd.DataFrame(records)