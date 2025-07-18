<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width="40%" height="40%" />
</p>

# 📘 Python - Inheritance

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

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following:

- What is a superclass, baseclass or parentclass  
- What is a subclass  
- How to list all attributes and methods of a class or instance  
- When can an instance have new attributes  
- How to inherit a class from another  
- How to define a class with multiple base classes  
- What is the default class every class inherits from  
- How to override a method or attribute inherited from the base class  
- Which attributes or methods are available by inheritance to subclasses  
- What is the purpose of inheritance  
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions  

---

## ✅ Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`  
- All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)  
- All files should end with a **new line**  
- First line of all files: `#!/usr/bin/python3`  
- A `README.md` file at the **root** of the project is **mandatory**  
- Code must follow **pycodestyle** (version `2.7.*`)  
- All files must be **executable**  
- File length will be tested using `wc`  

### Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`  
- All test files must end with a **new line**  
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

| File Name                 | Description                    |
|---------------------------|-------------------------------|
| `tests/1-my_list.txt`      | Doctest for `1-my_list.py`    |
| `tests/7-base_geometry.txt`| Doctest for `7-base_geometry.py` |

### 🐍 Python Scripts

| File Name                 | Description                                         |
|---------------------------|-----------------------------------------------------|
| `0-lookup.py`             | Lists available attributes and methods             |
| `0-main.py`               | Test script for `0-lookup.py`                       |
| `1-main.py`               | Test script for `1-my_list.py`                      |
| `1-my_list.py`            | Custom list class implementation                    |
| `2-is_same_class.py`      | Checks if object is exactly an instance of a class |
| `2-main.py`               | Test script for `2-is_same_class.py`                |
| `3-is_kind_of_class.py`   | Checks if object is instance or subclass            |
| `3-main.py`               | Test script for `3-is_kind_of_class.py`             |
| `4-inherits_from.py`      | Checks inheritance relationship                     |
| `4-main.py`               | Test script for `4-inherits_from.py`                |
| `5-base_geometry.py`      | Base geometry class with unimplemented methods      |
| `5-main.py`               | Test script for `5-base_geometry.py`                |
| `6-base_geometry.py`      | Base geometry class improvements                     |
| `6-main.py`               | Test script for `6-base_geometry.py`                |
| `7-base_geometry.py`      | Advanced base geometry class                         |
| `7-main.py`               | Test script for `7-base_geometry.py`                |
| `8-main.py`               | Test script for `8-rectangle.py`                     |
| `8-rectangle.py`          | Rectangle class inheriting from base geometry       |
| `9-main.py`               | Test script for `9-rectangle.py`                     |
| `9-rectangle.py`          | Advanced rectangle class with inheritance features  |
| `README.md`               | This file — project overview and documentation      |

---

## 📏 Python Style Guide — Pycodestyle (PEP8)

This project follows the official Python style guide: [PEP8](https://peps.python.org/pep-0008/), also known as `pycodestyle`.

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
focused on mastering Object-Oriented Programming (OOP) concepts through Inheritance in Python.

