import sqlite3
from student import Student
from storage import file_load


class studentmanager:
    def __init__(self):
        self.students = []

        # ensure table exists
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                grade TEXT
            )
        """)
        conn.commit()
        conn.close()

    def file_load(self):
        self.students = file_load()

    def add_student(self, student: Student):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                       (student.name, student.age, student.grade))
        conn.commit()
        conn.close()

    def get_students(self):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, grade FROM students")
        rows = cursor.fetchall()
        conn.close()
        return [Student(name, age, grade, sid) for sid, name, age, grade in rows]

    def update_student(self, student_id, name, age, grade):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?",
                       (name, age, grade, student_id))
        conn.commit()
        conn.close()

    def delete_student(self, student_id):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()

    def menu(self):
        while True:
            print("\n=== Student Management System ===")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                grade = input("Enter grade: ")
                student = Student(name, age, grade)
                self.add_student(student)
                print("✅ Student added.")

            elif choice == "2":
                students = self.get_students()
                print("\n--- Student List ---")
                for s in students:
                    print(
                        f"ID: {s.id} | Name: {s.name} | Age: {s.age} | Grade: {s.grade}")

            elif choice == "3":
                sid = int(input("Enter Student ID to update: "))
                name = input("New name: ")
                age = int(input("New age: "))
                grade = input("New grade: ")
                self.update_student(sid, name, age, grade)
                print("✅ Student updated.")

            elif choice == "4":
                sid = int(input("Enter Student ID to delete: "))
                self.delete_student(sid)
                print("✅ Student deleted.")

            elif choice == "5":
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    manager = studentmanager()
    manager.menu()
