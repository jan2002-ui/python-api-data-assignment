import requests
import sqlite3

# -----------------------------------
# 1. Fetch data from API
# -----------------------------------

API_URL = "https://openlibrary.org/search.json?q=python"

response = requests.get(API_URL, timeout=10)
response.raise_for_status()

data = response.json()
books = data["docs"]

print("API Status Code:", response.status_code)


# -----------------------------------
# 2. Connect to SQLite database
# -----------------------------------

connection = sqlite3.connect("database/books.db")

cursor = connection.cursor()

print("SQLite database connected successfully!")


# -----------------------------------
# 3. Create books table
# -----------------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        publication_year INTEGER
    )
""")

connection.commit()

print("Books table created successfully!")


# -----------------------------------
# 4. Insert first 5 books
# -----------------------------------

for book in books[:5]:

    title = book.get("title", "Unknown")

    author_list = book.get("author_name", ["Unknown"])
    author = author_list[0]

    year = book.get("first_publish_year")

    cursor.execute("""
        INSERT INTO books
        (title, author, publication_year)
        VALUES (?, ?, ?)
    """, (title, author, year))


connection.commit()

print("Books inserted successfully!")


# -----------------------------------
# 5. Retrieve data from database
# -----------------------------------

cursor.execute("""
    SELECT id, title, author, publication_year
    FROM books
""")

stored_books = cursor.fetchall()


# -----------------------------------
# 6. Display database records
# -----------------------------------

print("\nBooks stored in SQLite:")
print("-" * 70)

for book in stored_books:

    print(
        f"ID: {book[0]} | "
        f"Title: {book[1]} | "
        f"Author: {book[2]} | "
        f"Year: {book[3]}"
    )


# -----------------------------------
# 7. Close database connection
# -----------------------------------

connection.close()

print("\nDatabase connection closed.")