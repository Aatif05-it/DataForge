"""
CSV Export Example
"""

from dataforge import forge
from dataforge.exporter import Exporter

df = forge(
    rows=100,
    schema={
        "name": "name",
        "email": "email",
        "salary": "salary",
    },
)

Exporter().to_csv(
    df,
    "employees.csv",
)

print("CSV exported successfully.")