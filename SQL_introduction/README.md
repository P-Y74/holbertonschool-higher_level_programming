<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width="40%" height="40%"/>
</p>

# 🗃️ SQL - Introduction

## 📘 Introduction

This project provides a foundational understanding of **relational databases** and **SQL (Structured Query Language)** using **MySQL 8.0**. You'll learn how to create databases, manipulate tables, and retrieve data using SQL commands. The focus is on essential concepts such as DDL (Data Definition Language), DML (Data Manipulation Language), and query building techniques including subqueries and built-in functions.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain:

- ✅ What a database is
- ✅ What a relational database is
- ✅ What SQL stands for
- ✅ What MySQL is
- ✅ How to create a database in MySQL
- ✅ The difference between DDL and DML
- ✅ How to `CREATE` or `ALTER` a table
- ✅ How to `SELECT` data from a table
- ✅ How to `INSERT`, `UPDATE`, or `DELETE` data
- ✅ What subqueries are and when to use them
- ✅ How to use MySQL functions like `AVG()`, `COUNT()`, `SUM()`, etc.

---

## ⚙️ Project Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files executed on **Ubuntu 22.04 LTS** using **MySQL 8.0** (version 8.0.25)
- Each SQL file must:
  - End with a new line
  - Start with a comment describing the task
  - Contain a comment before each SQL query
  - Use **uppercase for SQL keywords** (e.g., `SELECT`, `INSERT`, `WHERE`, etc.)
- A `README.md` file is required at the root of the project
- File length will be tested using `wc`

---

## 🐬 Installing MySQL 8.0 on Ubuntu 20.04 LTS

To install MySQL on Ubuntu 20.04 LTS:

```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
sudo mysql_secure_installation
mysql --version
```

---

## 📂 Project Files and Descriptions

| File Name                          | Description                                         |
|-----------------------------------|-----------------------------------------------------|
| `README.md`                       | Project overview and objectives                    |
| `0-list_databases.sql`            | List all databases available in MySQL              |
| `1-create_database_if_missing.sql`| Create a database only if it does not exist        |
| `2-remove_database.sql`           | Delete a specific database                         |
| `3-list_tables.sql`               | List all tables in a specific database             |
| `4-first_table.sql`               | Describe the structure of a table                  |
| `5-full_table.sql`                | Display all records from a table                   |
| `6-list_values.sql`               | Select and display specific columns                |
| `7-insert_value.sql`              | Insert a new record into a table                   |
| `8-count_89.sql`                  | Count records where a value is 89                  |
| `9-full_creation.sql`             | Create a full table with multiple fields           |
| `10-top_score.sql`                | Select the record with the highest score           |
| `11-best_score.sql`               | Select the best score using a subquery             |
| `12-no_cheating.sql`              | Filter records with specific logic                 |
| `13-change_class.sql`             | Update a record’s value                            |
| `14-average.sql`                  | Calculate the average score                        |
| `15-groups.sql`                   | Group records by a specific column                 |
| `16-no_link.sql`                  | Filter out records based on a missing relation     |

---

## 🧪 Example SQL Syntax

Each file should follow a clean and consistent structure like the following:

```sql
-- This script selects all databases
SHOW DATABASES;
```
>✅ Make sure to begin each file with a task description comment and add inline comments before each query.

---


## ✅ SQL Best Practices

- 📌 **Begin every file with a task description comment**  
  This helps clarify the purpose of the file and makes the code more readable and maintainable.

- 💬 **Add inline comments above each SQL query**  
  Explain what the query is doing and why, especially for complex logic or subqueries.

- 🔠 **Use UPPERCASE for all SQL keywords**  
  Keep your code consistent and readable by writing keywords like `SELECT`, `FROM`, `WHERE`, `INSERT`, etc., in uppercase.

- ✨ **Keep queries clean, modular, and well-indented**  
  Break down complex statements and format them clearly, particularly when using joins, subqueries, or multiple conditions.

- 📐 **End each file with a newline**  
  Ensure proper formatting and compatibility with linters and version control systems.

---

## ✍️ Author

**P-Y74**  
🔗 [GitHub Profile](https://github.com/P-Y74)

---

## 🏫 Holberton School

This project is part of the **Foundations Curriculum** at **Holberton School**.
