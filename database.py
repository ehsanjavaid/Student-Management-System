import sqlite3
from student import Student

DB_NAME = "students.db"

# --- User Authentication Table ---
def connect_db():
    return sqlite3.connect(DB_NAME)

def create_user_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# --- Student Management ---
class DatabaseManager:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self._create_student_table()

    def connect_db(self):
        return sqlite3.connect(self.db_name)

    def _create_student_table(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT
            )
        """)
        conn.commit()
        conn.close()

    def add_student(self, student: Student):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
            (student.name, student.age, student.grade)
        )
        conn.commit()
        conn.close()

    def get_students(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, grade FROM students")
        rows = cursor.fetchall()
        conn.close()
        return [Student(name, age, grade, sid) for sid, name, age, grade in rows]

    def update_student(self, student_id, name, age, grade):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?",
            (name, age, grade, student_id)
        )
        conn.commit()
        conn.close()

    def delete_student(self, student_id):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()
