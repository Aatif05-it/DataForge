from pathlib import Path
import pandas as pd


class SQLExporter:

    def export(self, dataframe: pd.DataFrame, filename: str, table: str = "data"):
        path = Path(filename)

        if path.suffix != ".sql":
            path = path.with_suffix(".sql")

        columns = ", ".join(dataframe.columns)

        with open(path, "w", encoding="utf-8") as f:
            for _, row in dataframe.iterrows():
                values = []

                for value in row:
                    if isinstance(value, str):
                        value = value.replace("'", "''")
                        values.append(f"'{value}'")
                    elif pd.isna(value):
                        values.append("NULL")
                    else:
                        values.append(str(value))

                f.write(
                    f"INSERT INTO {table} ({columns}) VALUES ({', '.join(values)});\n"
                )

        return path