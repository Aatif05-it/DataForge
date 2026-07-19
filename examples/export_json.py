"""
JSON Export Example
"""

from dataforge import forge
from dataforge.exporter import Exporter

df = forge(
    rows=100,
    schema={
        "name": "name",
        "email": "email",
        "company": "company",
    },
)

Exporter().to_json(
    df,
    "employees.json",
)

print("JSON exported successfully.")