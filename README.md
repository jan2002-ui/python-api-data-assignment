# Python API Data Retrieval, Processing & SQLite Database

## 📌 Project Overview

This project demonstrates practical Python skills in **REST API integration, JSON data processing, SQLite database management, CSV data handling, data analysis, and visualization**.

The project contains three main modules:

* 📚 **API Data Retrieval & SQLite Storage**
* 📊 **Student Score Processing & Visualization**
* 📄 **CSV Data Import & SQLite Database**

---

## 🛠️ Technologies Used

* **Python 3.14.7**
* **Requests**
* **SQLite**
* **Matplotlib**
* **CSV**
* **JSON**
* **VS Code**
* **Git & GitHub**

---

## 📂 Project Structure

```text
python-api-data-assignment/
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
│   └── .gitkeep
│
├── output/
│   └── .gitkeep
│
├── .gitignore
└── README.md
```

> SQLite database files are excluded from GitHub using `.gitignore`.

---

# 📚 1. API Data Retrieval and SQLite Storage

### Description

This module retrieves book information from the **Open Library REST API** and stores the data in a local SQLite database.

### API

```text
https://openlibrary.org/search.json?q=python
```

### Data Retrieved

* Book Title
* Author
* Publication Year

### Database

```text
database/books.db
```

### Table

```text
books
```

### Run

```bash
python api_books/books_api.py
```

### Sample Output

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
```

---

# 📊 2. Student Score Processing and Visualization

### Description

This module processes student test scores, calculates the average score, and creates a bar chart using Matplotlib.

### Student Scores

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

### Run

```bash
python student_scores/student_scores.py
```

### Output

The program displays:

* Individual student scores
* Average score
* Bar chart comparing student scores
* Average score reference line

---

# 📄 3. CSV Data Import to SQLite

### Description

This module reads user information from a CSV file and stores it in a SQLite database.

### Input File

```text
csv_database/users.csv
```

### CSV Data

```csv
name,email
Arun,arun@gmail.com
Priya,priya@gmail.com
Rahul,rahul@gmail.com
Divya,divya@gmail.com
Karthik,karthik@gmail.com
```

### Database

```text
database/users.db
```

### Table

```text
users
```

### Run

```bash
python csv_database/csv_to_database.py
```

### Sample Output

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

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

## 2. Navigate to the Project

```bash
cd python-api-data-assignment
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

## 4. Install Required Packages

```bash
pip install requests matplotlib
```

---

# ▶️ Run the Project

### Books API

```bash
python api_books/books_api.py
```

### Student Scores

```bash
python student_scores/student_scores.py
```

### CSV to SQLite

```bash
python csv_database/csv_to_database.py
```

---

# 🎯 Skills Demonstrated

* Python Programming
* REST API Integration
* HTTP Requests
* JSON Parsing
* CSV Processing
* SQLite
* SQL Queries
* Database Management
* Data Processing
* Data Analysis
* Matplotlib Visualization
* File Handling
* Git & GitHub

---

# 📋 Assignment Requirements

| Requirement                 | Status      |
| --------------------------- | ----------- |
| Retrieve data from REST API | ✅ Completed |
| Store API data in SQLite    | ✅ Completed |
| Display book information    | ✅ Completed |
| Process student scores      | ✅ Completed |
| Calculate average score     | ✅ Completed |
| Create bar chart            | ✅ Completed |
| Read CSV file               | ✅ Completed |
| Insert CSV data into SQLite | ✅ Completed |
| Display database records    | ✅ Completed |

---

# 👩‍💻 Author

**Janani G.**

Data Analyst | Machine Learning Engineer

### Areas of Interest

* Data Analytics
* Python
* SQL
* Machine Learning
* Data Engineering
* Data Visualization
* Generative AI

---

## 📜 License

This project was developed for educational and assignment purposes.
