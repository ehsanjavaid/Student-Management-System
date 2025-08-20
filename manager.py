from student import Student
from storage import save_to_file, file_load
from database import sqlite3

class studentmanager:
    def __init__(self):
        self.students = []
    def file_load(self):
        self.students = file_load()

    def add_students(name, age, grade):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (?,?,?)", (name, age, grade))
        conn.commit()
        conn.close()
    
    def get_students():
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        conn.close()
        return rows
    def update_students(student_id, name, age, grade):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE students GET name = ?, age = ?, grade = ?", (name, age, grade, student_id))
        conn.commit()
        conn.close()
    def delete_students(student_id):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id))
        conn.commit()
        conn.close()
    
