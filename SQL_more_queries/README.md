<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width="40%" height="40%"/>
</p>


# 📊 SQL - More Queries

This project expands your knowledge of SQL by exploring more advanced concepts, including user management, data integrity constraints, subqueries, and table relationships using joins and unions.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain and apply the following concepts without external help:

### 📚 General

- What is a database user and how to create one in MySQL
- How to grant and revoke user privileges on databases or tables
- Understand and use `PRIMARY KEY` and `FOREIGN KEY` constraints
- Use `NOT NULL` and `UNIQUE` constraints to ensure data integrity
- Retrieve data across multiple tables with one SQL statement
- Utilize subqueries to filter or transform data
- Understand the difference between `JOIN` and `UNION` and when to use them

---

## ⚙️ Requirements

- ✅ Allowed editors: `vi`, `vim`, `emacs`
- ✅ All files will be run on **Ubuntu 20.04 LTS** using **MySQL 8.0 (8.0.25)**
- ✅ Every file must:
  - Start with a comment describing the task
  - Include a comment before each SQL query explaining what it does
  - End with a newline
  - Use **UPPERCASE** for SQL keywords (`SELECT`, `FROM`, `WHERE`, etc.)
  - Be counted using `wc` to verify length
- ✅ A `README.md` file at the root of the project is **mandatory**

---

## 📂 Project Files and Descriptions

| File Name                        | Description                                                  |
|----------------------------------|--------------------------------------------------------------|
| `0-privileges.sql`               | Grant privileges to a user                                   |
| `1-create_user.sql`              | Create a new MySQL user                                      |
| `2-create_read_user.sql`         | Create a user with read-only access                          |
| `3-force_name.sql`               | Enforce `NOT NULL` constraint on a column                    |
| `4-never_empty.sql`              | Add `NOT NULL` constraint to an existing table               |
| `5-unique_id.sql`                | Add a `UNIQUE` constraint to a column                        |
| `6-states.sql`                   | Create a `states` table with a `PRIMARY KEY`                 |
| `7-cities.sql`                   | Create a `cities` table with a `FOREIGN KEY` referencing `states` |
| `8-cities_of_california_subquery.sql` | Select cities from California using a subquery         |
| `9-cities_by_state_join.sql`     | Join `cities` and `states` tables to list cities by state   |
| `10-genre_id_by_show.sql`        | Get genre ID for each show using a join                     |
| `11-genre_id_all_shows.sql`      | List all shows with their genre IDs                         |
| `12-no_genre.sql`                | Find shows with no associated genre                         |
| `13-count_shows_by_genre.sql`    | Count shows by genre using `GROUP BY`                       |
| `14-my_genres.sql`               | List genres for a specific user                             |
| `15-comedy_only.sql`             | List all comedy shows only                                  |
| `16-shows_by_genre.sql`          | Group shows by genre                                        |
| `README.md`                      | Project documentation and objectives                        |

---

## ✅ SQL Code Style Guide

- 🔠 **Use UPPERCASE for SQL keywords**: `SELECT`, `INSERT`, `JOIN`, etc.
- 💬 **Add clear comments** before or beside every query.
- 📐 **Begin each file** with a comment describing the task.
- ✨ **Format your queries cleanly**, especially when using joins or subqueries.
- 📄 **End each file** with a newline character.

---

## 🧪 Example SQL Format

```sql
-- TASK: List all users in the MySQL database
SELECT User FROM mysql.user;

-- TASK: Create a new user with read-only access
CREATE USER 'read_user'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT ON your_database.* TO 'read_user'@'localhost';
```

---

## ✍️ Author

**P-Y74**  
🔗 [GitHub Profile](https://github.com/P-Y74)

---

## 🏫 Holberton School

This project is part of the **Foundations Curriculum** at **Holberton School**, designed to build a strong base in relational databases and SQL querying. You’ll gain hands-on experience with data integrity, **access control**, and **multi-table queries** — essential skills for back-end development and data management.
