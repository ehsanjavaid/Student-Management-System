import sqlite3
from student import Student


class DatabaseManager():
    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self._create_table()

    def connect_db(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
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
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                   (student.name, student.age, student.grade))
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
        cursor.execute("UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?",
                   (name, age, grade, student_id))
        conn.commit()
        conn.close()


    def delete_student(self, student_id):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()
