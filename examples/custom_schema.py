"""
Custom Schema Example
"""

from dataforge import forge

schema = {
    "employee_id": "uuid",
    "employee_name": "name",
    "employee_email": "email",
    "employee_phone": "phone",
    "company": "company",
    "salary": "salary",
    "office": "address",
    "password": "password",
}

df = forge(
    rows=20,
    schema=schema,
)

print(df)