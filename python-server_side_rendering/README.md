<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width="40%" height="40%"/>
</p>

# Python - Server-Side Rendering

This project explores **Server-Side Rendering (SSR)** using **Python** and **Flask**, as part of the learning curriculum at **Holberton School**.

SSR is a web development technique where HTML pages are fully rendered on the server before being sent to the client. Unlike client-side rendering (CSR), which relies heavily on JavaScript, SSR improves SEO, reduces time-to-content, and enhances overall performance and accessibility.

## 🚀 Learning Objectives

Through this project, you will:

- Understand the difference between server-side and client-side rendering.
- Discover the advantages of using SSR in modern web development.
- Implement SSR using the **Flask** framework.
- Use the **Jinja2 templating engine** to dynamically generate HTML content.
- Read and display data from various sources: **JSON**, **CSV**, and **SQLite**.
- Handle dynamic content, user input, and routing in Flask.

## 🛠️ What You'll Build

You will create a Flask-based web application that renders fully-formed HTML pages on the server using Jinja templates. The application will:

- Serve multiple HTML pages using a clean and reusable structure.
- Dynamically display data loaded from files and databases.
- Simulate real-world web app features such as product listings, about/contact pages, and more.

By the end of the project, you will have a functional, SEO-friendly, and scalable web application built entirely with server-side technologies.

## 📁 Project Structure

| File / Folder        | Description                                 |
|----------------------|---------------------------------------------|
| `00-main.py`         | Main Flask application entry point          |
| `README.md`          | Project documentation                       |
| `db_create.py`       | Script to create and populate the SQLite DB |
| `items.json`         | JSON data source                            |
| `products.csv`       | CSV data source                             |
| `products.db`        | SQLite database                             |
| `products.json`      | Another JSON data source                    |
| `task_00_intro.py`   | Introductory script                         |
| `task_01_jinja.py`   | Jinja templating practice                   |
| `task_02_logic.py`   | Logic handling with Flask                   |
| `task_03_files.py`   | File handling (JSON/CSV)                    |
| `task_04_db.py`      | Database integration                        |
| `template.txt`       | Template text file                          |
| `templates/`         | HTML templates directory                    |
| ├── `about.html`     | About page template                         |
| ├── `contact.html`   | Contact page template                       |
| ├── `footer.html`    | Reusable footer partial                     |
| ├── `header.html`    | Reusable header partial                     |
| ├── `index.html`     | Homepage template                           |
| ├── `items.html`     | Item listing page                           |
| └── `product_display.html` | Product display page template       |

## 🧠 Key Technologies

| Technology       | Purpose                                  |
|------------------|-------------------------------------------|
| Python 3         | Main programming language                |
| Flask            | Lightweight web framework for SSR        |
| Jinja2           | Templating engine for dynamic HTML       |
| SQLite3          | Lightweight relational database          |
| JSON & CSV       | Data source formats used in the project  |
| HTML5            | Markup language for web page structure   |

## 📚 How to Run the Project

1. **Install dependencies** (if not already installed):

   ```bash
   pip install Flask
   ```
2. **Run the main Flask application:**
   ```bash
   python run.py
   ```
3. **Open your web browser and go to:**
   http://localhost:5000

> ℹ️ Make sure your terminal is located in the project's root directory when running the Flask application.

---

## ✍️ Author

**P-Y74**  
🔗 [GitHub Profile](https://github.com/P-Y74)

---

## 🏫 About

This project is part of the **Full Stack Web Development** curriculum at **Holberton School**.

It focuses on mastering **Server-Side Rendering (SSR)** using Python and Flask, allowing you to build web applications that generate full HTML pages on the server. This approach improves:

- ✅ **Search engine optimization (SEO)**
- ✅ **Initial page load performance**
- ✅ **Accessibility for all users**

You will gain practical experience in templating, data handling, and clean architecture for scalable backend-rendered applications.
