"""
Basic Example
"""

import sys
from pathlib import Path

# Add project root to Python path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from dataforge import forge


def main():
    df = forge(
        rows=10,
        schema={
            "id": "uuid",
            "name": "name",
            "email": "email",
            "phone": "phone",
            "company": "company",
            "salary": "salary",
        },
    )

    print("=" * 80)
    print("DataForge Example")
    print("=" * 80)

    print("\nGenerated Dataset:\n")
    print(df)

    print("\nFirst 5 Rows:\n")
    print(df.head())

    print("\nDataset Information:\n")
    print(f"Rows    : {len(df)}")
    print(f"Columns : {len(df.columns)}")
    print(f"Shape   : {df.shape}")

    print("\nColumns:")
    print(list(df.columns))


if __name__ == "__main__":
    main()