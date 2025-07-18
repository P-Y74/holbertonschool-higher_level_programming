<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width="40%" height="40%"/>
</p>

# 🐍 Python - Object-Relational Mapping

This project bridges two essential domains in backend development: **Databases** and **Python**.

It consists of two parts:

1. **Direct MySQL interaction** using `MySQLdb`, a Python module to execute SQL queries directly.
2. **Object Relational Mapping (ORM)** using `SQLAlchemy`, where database operations are abstracted into Python objects — enabling clean, maintainable, and storage-agnostic code.

---

## 📚 Learning Objectives

By completing this project, you should be able to:

### 📌 General

- Connect to a MySQL database from a Python script
- Perform `SELECT` and `INSERT` operations from Python
- Understand what an **ORM** is and why it is useful
- Map a Python class to a MySQL table using **SQLAlchemy**

---

## ⚙️ Requirements

- ✅ Allowed editors: `vi`, `vim`, `emacs`
- ✅ Ubuntu 20.04 LTS
- ✅ Python 3.8.5
- ✅ `MySQLdb` version **2.0.x**
- ✅ `SQLAlchemy` version **1.4.x**
- ✅ Code must follow `pycodestyle` (2.7.\*) and end with a newline
- ✅ All scripts must be executable and start with:

```python
#!/usr/bin/python3
```
- ✅ A `README.md` file is **mandatory**.
- ✅ File length will be tested using `wc`.
- All your **modules** and **functions** must include proper documentation.

- Module Documentation

  - To check if a module is documented, run:

  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
  ```

  -To check if a function is properly documented, run the following command:

  ```bash
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  ```

  >ℹ️ **Documentation Requirements**
  >
  >Documentation must be a **complete sentence** that clearly explains the purpose of a **module**, **class**, or **function**.
  >
  > ❗ One-word or vague comments are not accepted — **clarity and length will be verified**.

---

## 🛠️ Setup

### 📦 Install MySQLdb and SQLAlchemy

```bash
pip install mysqlclient==2.0.*
pip install SQLAlchemy==1.4.*
```

---

## 📂 Project Files and Descriptions

| File Name                        | Description                                                      |
|---------------------------------|------------------------------------------------------------------|
| `0-select_states.py`             | Lists all states from the `hbtn_0e_0_usa` database using MySQLdb |
| `0-select_states.sql`            | SQL script to create the `states` table                          |
| `1-filter_states.py`             | Lists states with names starting with `N`                        |
| `2-my_filter_states.py`          | Takes an argument and displays matching state (vulnerable to SQL injection) |
| `3-my_safe_filter_states.py`     | Same as above but safe against SQL injection                     |
| `4-cities_by_state.py`           | Lists all cities grouped by state                                |
| `4-cities_by_state.sql`          | SQL script to create the `cities` table                          |
| `5-filter_cities.py`             | Displays cities of a state based on user input                   |
| `6-model_state.py`               | Defines `State` class mapped to the `states` table (ORM)         |
| `6-model_state.sql`              | SQL schema for `states`                                          |
| `7-model_state_fetch_all.py`     | Lists all `State` objects using SQLAlchemy                       |
| `7-model_state_fetch_all.sql`    | SQL script to populate `states`                                  |
| `8-model_state_fetch_first.py`   | Fetches the first `State` object                                 |
| `9-model_state_filter_a.py`      | Lists all `State` objects containing the letter `a`              |
| `10-model_state_my_get.py`       | Gets a state by name, prints ID or `Not found`                   |
| `11-model_state_insert.py`       | Adds a new `State` object (`Louisiana`) to the DB                |
| `12-model_state_update_id_2.py`  | Updates the name of the `State` with `id = 2`                    |
| `13-model_state_delete_a.py`     | Deletes all `State` objects containing the letter `a`            |
| `14-model_city_fetch_by_state.py`| Lists all cities and their associated states using relationships |
| `14-model_city_fetch_by_state.sql`| SQL script to create and link `cities` and `states` tables     |
| `model_city.py`                  | Defines `City` class linked to `State` via a foreign key         |
| `model_state.py`                 | Defines the SQLAlchemy `State` model (used across many files)    |
| `README.md`                     | Project documentation (this file)                                |

---

## 🧪 Example ORM Usage

```python
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup connection
engine = create_engine('mysql+mysqldb://user:pwd@localhost/db_name', pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

# Query example
states = session.query(State).order_by(State.id).all()
for state in states:
    print(f"{state.id}: {state.name}")
```

---

## 🧱 MySQL Mode vs ORM Mode

| Aspect         | SQL (MySQLdb)            | ORM (SQLAlchemy)               |
|----------------|--------------------------|-------------------------------|
| Query Style    | Manual SQL strings       | Python object manipulation    |
| Safety         | Needs manual escaping    | Safer via parameter binding   |
| Abstraction    | Low (SQL specific)       | High (Database agnostic)      |
| Learning Curve | Moderate (SQL knowledge) | Slightly higher initially     |

---

## 📏 Code Style Guide

- 🔠 Use **UPPERCASE** for all SQL keywords (SELECT, WHERE, INSERT, etc.)
- 💬 Add comments before every script and query explaining its purpose
- 📐 Begin every file with a task description comment
- ✨ Maintain clear structure and indentation in your code
- 🧼 Follow **PEP8** (via `pycodestyle`) for Python scripts

---

## ✍️ Author

**P-Y74**  
🔗 [GitHub Profile](https://github.com/P-Y74)

---

## 🏫 Holberton School

This project is part of the **Foundations Curriculum** at **Holberton School**, and a stepping stone to building robust Python backends using relational databases.
