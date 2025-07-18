<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width=40% height=40%/>
</p>

# 📘 Python - Test-driven Development

## 🧠 Background Context

> 🔔 **Important Notice on Intranet Checks**
>
> Starting from this project:
>
> - Always write **documentation** (modules + functions) and **tests first** — before writing code.
> - Intranet checks are **locked** until the first deadline to encourage **TDD** and thorough edge-case handling.
> - You are encouraged to **collaborate on test cases** — not implementations.
> - **Never trust the user input** — think about all possible edge cases.

---

## 📚 Resources

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (up to *26.2.3.7. Warnings*)
- [doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following:

- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

---

## ✅ Requirements

### General Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Files must end with a **new line**
- First line of all files: `#!/usr/bin/python3`
- A `README.md` file at the **root** of the project is mandatory
- Code must follow **pycodestyle** (version `2.7.*`)
- All files must be **executable**
- File length will be tested using `wc`

### Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`
- All files must end with a **new line**
- All test files must be inside a **`tests/`** folder
- Test files must have a `.txt` extension
- Run tests with:

```bash
python3 -m doctest ./tests/*
```

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

## 📁 Project Files and Descriptions

### 🧪 `tests/` Folder

| File Name                      | Description                             |
|-------------------------------|-----------------------------------------|
| `tests/0-add_integer.txt`     | Doctest for `0-add_integer.py`          |
| `tests/2-matrix_divided.txt`  | Doctest for `2-matrix_divided.py`       |
| `tests/3-say_my_name.txt`     | Doctest for `3-say_my_name.py`          |
| `tests/4-print_square.txt`    | Doctest for `4-print_square.py`         |
| `tests/5-text_indentation.txt`| Doctest for `5-text_indentation.py`     |
| `tests/6-max_integer_test.py` | Unittest module for `6-max_integer.py`  |

### 🐍 Python Scripts

| File Name                 | Description                                          |
|---------------------------|------------------------------------------------------|
| `0-add_integer.py`        | Adds two integers                                    |
| `0-main.py`               | Test script for `0-add_integer.py`                  |
| `2-matrix_divided.py`     | Divides all elements of a matrix                    |
| `2-main.py`               | Test script for `2-matrix_divided.py`               |
| `3-say_my_name.py`        | Prints `"My name is <first name> <last name>"`      |
| `3-main.py`               | Test script for `3-say_my_name.py`                  |
| `4-print_square.py`       | Prints a square with the character `#`              |
| `4-main.py`               | Test script for `4-print_square.py`                 |
| `5-text_indentation.py`   | Prints text with 2 new lines after `.`, `?`, `:`    |
| `5-main.py`               | Test script for `5-text_indentation.py`             |
| `6-max_integer.py`        | Finds the max integer in a list                     |
| `6-main.py`               | Test script for `6-max_integer.py`                  |
| `README.md`               | Project overview and documentation                  |

---

## 📏 Python Style Guide — Pycodestyle (PEP8)

This project follows the **official Python style guide**: [PEP8](https://peps.python.org/pep-0008/), also known as `pycodestyle`.

To check your code style compliance, run:

```bash
pycodestyle your_script.py
```

---

## 📏 Python Style Guide — PEP8

PEP8 ensures that your Python code is:

- ✅ **Readable**
- ✅ **Consistent**
- ✅ **Easy to maintain**

---

## ✍️ Author

**P-Y74**  
🔗 [GitHub Profile](https://github.com/P-Y74)

---

## 🏫 Holberton School

This project is part of the **Foundations Curriculum** at **Holberton School**,  
focused on mastering **Test-Driven Development (TDD)** in Python.


