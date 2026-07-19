"""
JSON Exporter

Export DataFrame to JSON.
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd


class JSONExporter:
    """
    Export DataFrame to JSON.
    """

    def export(
        self,
        dataframe: pd.DataFrame,
        filename: str,
        orient: str = "records",
        indent: int = 4,
    ) -> Path:

        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Expected pandas DataFrame.")

        path = Path(filename)

        if path.suffix.lower() != ".json":
            path = path.with_suffix(".json")

        dataframe.to_json(
            path,
            orient=orient,
            indent=indent,
        )

        return path