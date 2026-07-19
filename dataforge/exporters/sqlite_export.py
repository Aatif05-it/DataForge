"""
SQLite Exporter

Export DataFrame to SQLite.
"""

from __future__ import annotations

from pathlib import Path
import sqlite3

import pandas as pd


class SQLiteExporter:
    """
    Export DataFrame to SQLite.
    """

    def export(
        self,
        dataframe: pd.DataFrame,
        database: str,
        table: str = "data",
        if_exists: str = "replace",
    ) -> Path:

        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Expected pandas DataFrame.")

        path = Path(database)

        if path.suffix.lower() != ".db":
            path = path.with_suffix(".db")

        connection = sqlite3.connect(path)

        dataframe.to_sql(
            table,
            connection,
            if_exists=if_exists,
            index=False,
        )

        connection.commit()
        connection.close()

        return path