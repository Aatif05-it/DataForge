# DataForge

> Generate realistic synthetic datasets with a simple and powerful API.

DataForge is a modern Python library for generating realistic fake datasets for testing,
machine learning, software development, education, and demonstrations.

---

## Features

- Generate thousands of records in seconds
- Simple and intuitive API
- Export to CSV
- Export to JSON
- Export to Excel (.xlsx)
- Export to SQLite
- Custom schemas
- Built on top of Pandas
- Cross-platform

---

## Installation

```bash
pip install dataforge
```

Or install locally

```bash
git clone https://github.com/yourusername/DataForge.git

cd DataForge

pip install -e .
```

---

## Quick Start

```python
from dataforge import forge

df = forge(
    rows=100,
    schema={
        "name": "name",
        "email": "email",
        "phone": "phone",
        "salary": "salary"
    }
)

print(df.head())
```

---

## Example Output

| Name | Email | Phone | Salary |
|------|-------|--------|---------|
| John Smith | john@example.com | +1 555-1234 | 65000 |
| Alice Brown | alice@test.com | +1 555-5678 | 72000 |

---

## Export CSV

```python
from dataforge import forge

df = forge(
    rows=500,
    schema={
        "name":"name",
        "email":"email"
    }
)

df.to_csv("users.csv", index=False)
```

---

## Export Excel

```python
df.to_excel("users.xlsx", index=False)
```

---

## Export JSON

```python
df.to_json("users.json")
```

---

## Roadmap

- CSV Export
- JSON Export
- Excel Export
- SQLite Export
- YAML Schema
- REST API
- CLI Tool
- AI Dataset Generator
- PostgreSQL Export
- MongoDB Export

---

## Project Structure

```
DataForge/
│
├── dataforge/
├── examples/
├── tests/
├── docs/
├── README.md
├── setup.py
└── pyproject.toml
```

---

## Requirements

- Python 3.10+
- Pandas
- Faker
- OpenPyXL

---

## License

MIT License

---

## Author

Khan Aatif

---

## Contributing

Pull requests are welcome.

If you find bugs or have feature requests, please open an issue.