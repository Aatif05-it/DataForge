import unittest

from dataforge.schema import Schema


class TestSchema(unittest.TestCase):

    def test_valid_schema(self):

        schema = Schema(
            {
                "name": "name",
                "email": "email",
            }
        )

        self.assertTrue(schema.validate())

    def test_invalid_provider(self):

        with self.assertRaises(ValueError):

            Schema(
                {
                    "name": "unknown_provider",
                }
            ).validate()


if __name__ == "__main__":
    unittest.main()