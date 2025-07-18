<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width="40%" height="40%"/>
</p>

# 📘 Python - Input/Output

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome  
- How to open a file  
- How to write text in a file  
- How to read the full content of a file  
- How to read a file line by line  
- How to move the cursor in a file  
- How to make sure a file is closed after using it  
- What is and how to use the `with` statement  
- What is JSON  
- What is serialization  
- What is deserialization  
- How to convert a Python data structure to a JSON string  
- How to convert a JSON string to a Python data structure  
- How to access command line parameters in a Python script  

---

## ⚙️ Requirements

- Allowed editors: `vi`, `vim`, `emacs`  
- All your files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8.5)  
- All your files should end with a new line  
- The first line of all your files should be exactly:  
  ```bash
  #!/usr/bin/python3
  ```
- A `README.md` file, at the root of the project folder, is **mandatory**  
- Your code should follow the **pycodestyle** (version 2.7.*)  
- All your files must be **executable**  
- The length of your files will be tested using `wc`  

---

## 🧪 Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`  
- All your test files should end with a new line  
- All your test files should be inside a folder named `tests`  
- All your test files should be text files (`.txt` extension)
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

| File Name              | Description                                             |
|------------------------|---------------------------------------------------------|
| `README.md`            | Project overview and documentation                       |
| `0-main.py`            | Test script for `0-read_file.py`                        |
| `0-read_file.py`       | Function to read the entire content of a file           |
| `1-main.py`            | Test script for `1-write_file.py`                       |
| `1-write_file.py`      | Function to write text to a file                         |
| `2-main.py`            | Test script for `2-append_write.py`                     |
| `2-append_write.py`    | Function to append text to a file                        |
| `3-main.py`            | Test script for `3-to_json_string.py`                   |
| `3-to_json_string.py`  | Converts Python data structures to JSON strings         |
| `4-main.py`            | Test script for `4-from_json_string.py`                 |
| `4-from_json_string.py`| Converts JSON strings to Python data structures         |
| `5-main.py`            | Test script for `5-save_to_json_file.py`                |
| `5-save_to_json_file.py`| Saves Python objects to a JSON file                      |
| `6-main.py`            | Test script for `6-load_from_json_file.py`              |
| `6-load_from_json_file.py`| Loads Python objects from a JSON file                  |
| `7-add_item.py`        | Adds items to a Python list and saves to JSON file      |
| `8-main.py`            | Test scripts for classes and JSON serialization (multiple) |
| `8-main_2.py`          | Additional test script for class serialization           |
| `8-class_to_json.py`   | Converts class objects to JSON serializable dictionaries |
| `8-my_class.py`        | Example class to be serialized                            |
| `8-my_class_2.py`      | Extended example class for serialization                  |
| `9-main.py`            | Test script for `9-student.py`                           |
| `9-student.py`         | Student class demonstrating JSON serialization           |
| `10-main.py`           | Test script for `10-student.py`                          |
| `10-student.py`        | Extended Student class with more features                 |
| `11-main.py`           | Test script for `11-student.py`                          |
| `11-student.py`        | Further extension of Student class                        |
| `12-main.py`           | Test script for `12-pascal_triangle.py`                 |
| `12-pascal_triangle.py`| Function generating Pascal's Triangle                     |
| `my_file_0.txt`        | Sample text file used for input/output tests             |

---

## 📏 Python Style Guide — Pycodestyle (PEP8)

This project follows the official Python style guide: **PEP8**, also known as **pycodestyle**.

To check your code style compliance, run:

```bash
pycodestyle your_script.py
```

---

## 📏 PEP8 Compliance

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

This project is part of the **Foundations Curriculum** at **Holberton School**, focused on mastering file I/O and JSON serialization/deserialization in Python.
