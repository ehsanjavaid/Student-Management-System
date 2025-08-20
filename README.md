# 🎓 Student Management System (Python + SQLite)

A simple command-line Student Management System built with Python and SQLite.  
It allows you to **add, view, update, and delete student records** stored in a local database (`students.db`).

---

## ✨ Features
- 📥 Add new students (name, age, grade)
- 📋 View all students
- ✏️ Update student details
- ❌ Delete a student
- 💾 Persistent storage using SQLite

---

## 📂 Project Structure

```bash
Student Management System/
│── manager.py # Main program (menu + DB operations)
│── student.py # Student class definition
│── storage.py # (Optional) file loading utility
│── students.db # SQLite database (created automatically)
│── README.md # Project documentation
 ```
 
---

## ⚙️ Requirements
- Python 3.8+
- No external libraries needed (uses built-in `sqlite3`)

---

## 🚀 How to Run
1. Clone or download the project.
2. (Optional but recommended) Create a virtual environment:

```bash
   python -m venv .venv
   source .venv/bin/activate   # On Linux/Mac
   .venv\Scripts\activate      # On Windows
```
Run the program:
```bash
python manager.py
```
📖 Usage

When you run the program, you’ll see a menu:

```bash
=== Student Management System ===
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
```
1. Add Student

Enter student name, age, and grade → saved in database.

2. View Students

Displays a list of all students in the format:
```bash
ID: 1 | Name: Ali | Age: 24 | Grade: A
```

3. Update Student

Enter Student ID → update name, age, grade.

4. Delete Student

Enter Student ID → student is removed from the database.

5. Exit

Closes the program.

🛠 Example Run

```bash
=== Student Management System ===
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
Enter choice: 1
Enter name: Ali
Enter age: 24
Enter grade: A
✅ Student added.

Enter choice: 2
--- Student List ---
ID: 1 | Name: Ali | Age: 24 | Grade: A

```
📌 Notes

The database (students.db) is automatically created if it doesn’t exist.

The Student class in student.py must define:

```bash
class Student:
    def __init__(self, name, age, grade, sid=None):
        self.id = sid
        self.name = name
        self.age = age
        self.grade = grade

```

📜 License

This project is free to use for learning and personal projects.

---

👉 Do you want me to also include the **final cleaned `manager.py`** code (ready to run), so you have README + working code in sync?

