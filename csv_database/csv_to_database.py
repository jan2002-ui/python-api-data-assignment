import csv
import sqlite3


# -----------------------------------
# 1. Connect to SQLite
# -----------------------------------

connection = sqlite3.connect(
    "database/users.db"
)

cursor = connection.cursor()

print(
    "SQLite database connected successfully!"
)


# -----------------------------------
# 2. Create users table
# -----------------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")

connection.commit()

print(
    "Users table created successfully!"
)


# -----------------------------------
# 3. Read CSV and insert data
# -----------------------------------

with open(
    "csv_database/users.csv",
    "r",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        name = row["name"].strip()
        email = row["email"].strip()

        cursor.execute("""
            INSERT OR IGNORE INTO users
            (name, email)
            VALUES (?, ?)
        """, (name, email))


connection.commit()

print(
    "CSV data inserted successfully!"
)


# -----------------------------------
# 4. Retrieve users
# -----------------------------------

cursor.execute("""
    SELECT id, name, email
    FROM users
""")

users = cursor.fetchall()


# -----------------------------------
# 5. Display users
# -----------------------------------

print("\nUsers stored in SQLite:")
print("-" * 60)

for user in users:

    print(
        f"ID: {user[0]} | "
        f"Name: {user[1]} | "
        f"Email: {user[2]}"
    )


# -----------------------------------
# 6. Close database
# -----------------------------------

connection.close()

print("\nDatabase connection closed.")