from pathlib import Path
import pandas as pd


class TXTExporter:

    def export(
        self,
        dataframe: pd.DataFrame,
        filename: str,
        separator: str = "\t",
    ):

        path = Path(filename)

        if path.suffix != ".txt":
            path = path.with_suffix(".txt")

        dataframe.to_csv(
            path,
            sep=separator,
            index=False,
        )

        return path