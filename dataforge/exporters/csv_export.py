"""
CSV Exporter

Export pandas DataFrame to CSV.
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd


class CSVExporter:
    """
    Export DataFrame to CSV.

    Example
    -------
    exporter = CSVExporter()

    exporter.export(df, "users.csv")
    """

    def export(
        self,
        dataframe: pd.DataFrame,
        filename: str,
        index: bool = False,
        encoding: str = "utf-8",
    ) -> Path:
        """
        Export DataFrame to CSV.
        """

        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Expected pandas DataFrame.")

        path = Path(filename)

        if path.suffix.lower() != ".csv":
            path = path.with_suffix(".csv")

        dataframe.to_csv(
            path,
            index=index,
            encoding=encoding,
        )

        return path

    def append(
        self,
        dataframe: pd.DataFrame,
        filename: str,
        encoding: str = "utf-8",
    ) -> Path:
        """
        Append rows to existing CSV.
        """

        path = Path(filename)

        dataframe.to_csv(
            path,
            mode="a",
            header=not path.exists(),
            index=False,
            encoding=encoding,
        )

        return path