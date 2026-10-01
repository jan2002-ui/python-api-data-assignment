# Python API Data Retrieval, Processing & SQLite Database

## 📌 Project Overview

This project demonstrates practical Python skills in **REST API data retrieval, JSON data processing, SQLite database management, CSV data import, data analysis, and visualization**.

The project is divided into three modules:

1. **API Data Retrieval and Storage** – Fetch book information from an external REST API and store it in SQLite.
2. **Data Processing and Visualization** – Process student test scores, calculate the average score, and visualize the results using a bar chart.
3. **CSV Data Import to Database** – Read user information from a CSV file and insert the data into a SQLite database.

---

## 🎯 Objectives

* Retrieve data from a REST API using Python.
* Parse and process JSON responses.
* Store structured data in SQLite databases.
* Read and process CSV files.
* Perform basic data analysis using Python.
* Calculate average student scores.
* Create data visualizations using Matplotlib.
* Demonstrate SQL operations using Python's SQLite library.
* Organize Python projects using a modular folder structure.

---

## 🛠️ Technologies Used

| Technology    | Purpose                             |
| ------------- | ----------------------------------- |
| Python 3.14.7 | Programming language                |
| Requests      | REST API communication              |
| SQLite        | Local database storage              |
| Matplotlib    | Data visualization                  |
| CSV           | CSV file processing                 |
| JSON          | API response processing             |
| VS Code       | Development environment             |
| Git/GitHub    | Version control and project sharing |

### Python Libraries

```text
requests
matplotlib
sqlite3
csv
json
```

> `sqlite3`, `csv`, and `json` are included with Python and do not require separate installation.

---

# 📂 Project Structure

```text
Python API Data assignment/
│
├── api_books/
│   └── books_api.py
│
├── student_scores/
│   └── student_scores.py
│
├── csv_database/
│   ├── users.csv
│   └── csv_to_database.py
│
├── database/
│   ├── books.db
│   └── users.db
│
├── output/
│
└── README.md
```

---

# 📚 Part 1 – API Data Retrieval and SQLite Storage

## Description

The first module retrieves book information from the **Open Library REST API**.

The application:

1. Sends a GET request to the API.
2. Receives the JSON response.
3. Extracts book title, author, and publication year.
4. Creates a SQLite database.
5. Creates a `books` table.
6. Inserts book records into the database.
7. Retrieves and displays the stored records.

### API Used

```text
https://openlibrary.org/search.json?q=python
```

### Database Table

```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    publication_year INTEGER
);
```

### Python File

```text
api_books/books_api.py
```

### Run the Program

From the project root directory:

```powershell
python api_books\books_api.py
```

### Expected Output

```text
API Status Code: 200
SQLite database connected successfully!
Books table created successfully!
Books inserted successfully!

Books stored in SQLite:
----------------------------------------------------------------------
ID: 1 | Title: Learning Python | Author: Mark Lutz | Year: 1999
ID: 2 | Title: Python For Data Analysis | Author: Wes McKinney | Year: 2012
ID: 3 | Title: Fluent Python | Author: Luciano Ramalho | Year: 2015
ID: 4 | Title: Black Hat Python | Author: Justin Seitz | Year: 2014
ID: 5 | Title: Python Cookbook | Author: Alex Martelli | Year: 2002

Database connection closed.
```

Database generated:

```text
database/books.db
```

---

# 📊 Part 2 – Student Score Processing and Visualization

## Description

The second module processes student test score data and performs basic statistical analysis.

The application:

1. Stores student score data.
2. Extracts student names and scores.
3. Calculates the average score.
4. Displays individual student scores.
5. Creates a bar chart.
6. Displays the average score as a reference line.

### Student Data

| Student | Score |
| ------- | ----: |
| Arun    |    78 |
| Priya   |    85 |
| Rahul   |    92 |
| Divya   |    88 |
| Karthik |    74 |

### Average Score

```text
83.40
```

### Python File

```text
student_scores/student_scores.py
```

### Run the Program

```powershell
python student_scores\student_scores.py
```

### Expected Output

```text
Student Test Scores
----------------------------------------
Arun: 78
Priya: 85
Rahul: 92
Divya: 88
Karthik: 74
----------------------------------------
Average Score: 83.40
```

The program also generates a bar chart comparing the scores of all students and displays the average score.

---

# 📄 Part 3 – CSV Data Import to SQLite

## Description

The third module demonstrates how to import structured CSV data into a SQLite database.

The application:

1. Connects to SQLite.
2. Creates a `users` table.
3. Reads data from `users.csv`.
4. Extracts name and email information.
5. Inserts the records into SQLite.
6. Retrieves the stored records.
7. Displays the database contents.

### CSV File

```text
csv_database/users.csv
```

### CSV Structure

```csv
name,email
Arun,arun@gmail.com
Priya,priya@gmail.com
Rahul,rahul@gmail.com
Divya,divya@gmail.com
Karthik,karthik@gmail.com
```

### Database Table

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
```

The `UNIQUE` constraint on the email field helps prevent duplicate email records.

### Python File

```text
csv_database/csv_to_database.py
```

### Run the Program

```powershell
python csv_database\csv_to_database.py
```

### Expected Output

```text
SQLite database connected successfully!
Users table created successfully!
CSV data inserted successfully!

Users stored in SQLite:
------------------------------------------------------------
ID: 1 | Name: Arun | Email: arun@gmail.com
ID: 2 | Name: Priya | Email: priya@gmail.com
ID: 3 | Name: Rahul | Email: rahul@gmail.com
ID: 4 | Name: Divya | Email: divya@gmail.com
ID: 5 | Name: Karthik | Email: karthik@gmail.com

Database connection closed.
```

Database generated:

```text
database/users.db
```

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

```powershell
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project:

```powershell
cd "Python API Data assignment"
```

## 2. Create a Virtual Environment

```powershell
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

## 3. Install Required Libraries

```powershell
pip install requests matplotlib
```

## 4. Verify Python Installation

```powershell
python --version
```

Example:

```text
Python 3.14.7
```

---

# ▶️ How to Run the Project

Run each module separately from the project root.

### Part 1 – Books API

```powershell
python api_books\books_api.py
```

### Part 2 – Student Scores

```powershell
python student_scores\student_scores.py
```

### Part 3 – CSV to SQLite

```powershell
python csv_database\csv_to_database.py
```

---

# 🗄️ Database Information

## Books Database

Database:

```text
database/books.db
```

Table:

```text
books
```

Columns:

```text
id
title
author
publication_year
```

## Users Database

Database:

```text
database/users.db
```

Table:

```text
users
```

Columns:

```text
id
name
email
```

---

# 🔄 Project Workflow

```text
                 ┌─────────────────────┐
                 │   External REST API  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Python Requests   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   JSON Processing   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    SQLite Database  │
                 └─────────────────────┘


                 ┌─────────────────────┐
                 │   Student Dataset   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Python Data Analysis│
                 └──────────┬──────────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
          Average Calculation      Bar Chart


                 ┌─────────────────────┐
                 │      users.csv      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Python CSV Reader   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    SQLite Database  │
                 └─────────────────────┘
```

---

# 🔐 Data Handling

The project demonstrates basic structured data handling practices:

* Parameterized SQL queries are used for database insertion.
* CSV values are read using Python's `csv.DictReader`.
* Database connections are explicitly closed after operations.
* The users database uses a unique constraint on email addresses.
* API responses are converted from JSON into Python data structures before processing.

---

# 📈 Skills Demonstrated

This project demonstrates the following technical skills:

* Python Programming
* REST API Integration
* HTTP GET Requests
* JSON Parsing
* CSV Processing
* SQLite Database Management
* SQL Queries
* Database Table Creation
* Data Insertion and Retrieval
* Data Analysis
* Average Calculation
* Data Visualization
* Matplotlib
* Exception-Aware Data Processing
* File and Folder Management
* Git/GitHub Project Organization

---

# 🚀 Future Enhancements

Possible improvements include:

* Add comprehensive API error handling.
* Add duplicate prevention for book records.
* Save generated charts automatically to the `output` directory.
* Add more statistical calculations such as median and standard deviation.
* Add database search and filtering functionality.
* Add unit tests using `pytest`.
* Add logging instead of relying only on console messages.
* Add a web interface for viewing database records.
* Add automated data validation.
* Add a requirements file for dependency management.

---

# 📌 Assignment Requirements Covered

| Requirement                   | Implementation   | Status      |
| ----------------------------- | ---------------- | ----------- |
| Fetch book data from REST API | Open Library API | ✅ Completed |
| Store book data in SQLite     | `books.db`       | ✅ Completed |
| Display title, author, year   | Python + SQL     | ✅ Completed |
| Process student scores        | Python           | ✅ Completed |
| Calculate average score       | Python           | ✅ Completed |
| Create bar chart              | Matplotlib       | ✅ Completed |
| Read CSV user data            | `users.csv`      | ✅ Completed |
| Insert CSV data into SQLite   | `users.db`       | ✅ Completed |
| Display stored user data      | Python + SQL     | ✅ Completed |

---

# 👩‍💻 Author

**Janani G.**

Data Analyst / Machine Learning Engineer

### Technical Interests

* Python
* Data Analytics
* SQL
* Machine Learning
* Data Engineering
* Generative AI
* Data Visualization

---

# 📜 License

This project was created for educational and assignment purposes.
