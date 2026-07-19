import argparse

from dataforge import forge
from dataforge.exporter import Exporter


def main():
    parser = argparse.ArgumentParser(
        prog="dataforge",
        description="Generate fake datasets"
    )

    parser.add_argument("--rows", type=int, default=10)
    parser.add_argument(
        "--format",
        choices=["csv", "json", "xlsx", "txt", "sql", "db"],
        default="csv",
    )
    parser.add_argument("--output", default="dataset")

    args = parser.parse_args()

    df = forge(
        rows=args.rows,
        schema={
            "id": "uuid",
            "name": "name",
            "email": "email",
            "phone": "phone",
            "company": "company",
            "salary": "salary",
        },
    )

    exporter = Exporter()

    if args.format == "csv":
        exporter.to_csv(df, args.output + ".csv")

    elif args.format == "json":
        exporter.to_json(df, args.output + ".json")

    elif args.format == "xlsx":
        exporter.to_excel(df, args.output + ".xlsx")

    elif args.format == "txt":
        exporter.to_txt(df, args.output + ".txt")

    elif args.format == "sql":
        exporter.to_sql(df, args.output + ".sql", table="employees")

    elif args.format == "db":
        exporter.to_sqlite(df, args.output + ".db", table="employees")

    print(f"Generated {args.rows} rows.")
    print(f"Saved to {args.output}.{args.format}")


if __name__ == "__main__":
    main()
