<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width=40% height=40%/>
</p>

# 🐍 Python - Import & Modules

This project is part of the Holberton School Foundation curriculum and introduces a core concept of modular programming in Python: **importing functions and using modules**.

---

## 📚 What You’ll Learn

- Why Python programming is awesome 😎
- How to import functions from another file
- How to use imported functions
- How to create and use your own modules
- How to use the built-in `dir()` function
- How to avoid code from executing when a file is imported
- How to use command-line arguments in Python

---

## 🔍 Introduction: Imports & Modules in Python

In Python, a **module** is simply a file containing Python code (with a `.py` extension). You can **reuse** the functions, variables, or classes defined in that file by **importing** them into another script.

### 🧩 Why use modules?

- 🧱 Code organization
- ♻️ Reusability
- 📦 Separation of concerns
- 🧪 Easier testing and debugging

### 🔁 Example of import

Suppose you have a file `math_utils.py`:

```python
def add(a, b):
    return a + b
```

You can reuse this function in another file:

```python
from math_utils import add

print(add(2, 3))  # Output: 5
```

### 🛑 Prevent code execution on import

Use this pattern to avoid running code when the module is imported:

```python
if __name__ == "__main__":
    # This block runs only if the script is executed directly
    main()
```

---

## 🛠️ Requirements

- Allowed editors: `vi`, `vim`, `emacs`  
- All files will be interpreted using Python 3.10 on Ubuntu 22.04 LTS  
- The first line of all Python files should be:

```python
#!/usr/bin/python3
```

---

All files must:

- End with a new line  
- Be executable  
- Respect pycodestyle (version 2.7.*)  
- Be tested with the `wc` command for length  
- A `README.md` file at the root of the project is mandatory  

---

## 📏 Python Style Guide — Pycodestyle (PEP8)

This project follows the official PEP8 style guide, also known as pycodestyle.

Although Holberton does not strictly enforce all rules early on, learning and following these standards helps you write:

✅ Clean  
✅ Readable  
✅ Professional Python code  

To check your code style:

```bash
pycodestyle your_script.py
```

---

## ✍️ Author

P-Y74  
[GitHub Profile](https://github.com/P-Y74)

---

## 🏫 Holberton School

This project is part of the Foundations Curriculum at Holberton School, focusing on building strong fundamentals in Python modules, imports, and script execution control.

