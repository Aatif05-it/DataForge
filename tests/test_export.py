import unittest

from pathlib import Path

from dataforge import forge
from dataforge.exporter import Exporter


class TestExporter(unittest.TestCase):

    def test_csv_export(self):

        df = forge(
            rows=5,
            schema={
                "name": "name",
            },
        )

        file = Exporter().to_csv(
            df,
            "test.csv",
        )

        self.assertTrue(Path(file).exists())

    def test_json_export(self):

        df = forge(
            rows=5,
            schema={
                "email": "email",
            },
        )

        file = Exporter().to_json(
            df,
            "test.json",
        )

        self.assertTrue(Path(file).exists())


if __name__ == "__main__":
    unittest.main()