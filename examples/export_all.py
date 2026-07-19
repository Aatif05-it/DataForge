import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from dataforge import forge
from dataforge.exporter import Exporter


df = forge(
    rows=20,
    schema={
        "id": "uuid",
        "name": "name",
        "email": "email",
        "phone": "phone",
        "company": "company",
        "salary": "salary",
    },
)

Exporter().export_all(
    dataframe=df,
    name="employees",
    table="employees",
)

print(df.head())