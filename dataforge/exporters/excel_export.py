"""
Excel Exporter

Export DataFrame to Excel.
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd


class ExcelExporter:
    """
    Export DataFrame to Excel.
    """

    def export(
        self,
        dataframe: pd.DataFrame,
        filename: str,
        sheet_name: str = "Sheet1",
        index: bool = False,
    ) -> Path:

        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Expected pandas DataFrame.")

        path = Path(filename)

        if path.suffix.lower() != ".xlsx":
            path = path.with_suffix(".xlsx")

        dataframe.to_excel(
            path,
            sheet_name=sheet_name,
            index=index,
        )

        return path