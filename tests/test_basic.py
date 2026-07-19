import unittest

from dataforge import forge


class TestBasic(unittest.TestCase):

    def test_dataframe_rows(self):

        df = forge(
            rows=50,
            schema={
                "name": "name",
                "email": "email",
            },
        )

        self.assertEqual(len(df), 50)

    def test_columns(self):

        df = forge(
            rows=10,
            schema={
                "name": "name",
                "email": "email",
            },
        )

        self.assertIn("name", df.columns)

        self.assertIn("email", df.columns)


if __name__ == "__main__":
    unittest.main()