from student import Student
from database import DatabaseManager
from tabulate import tabulate
from auth import add_user, login
from database import create_user_table, connect_db

class StudentManager:
    def __init__(self, role):
        self.db = DatabaseManager()
        self.role = role

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
                if self.role != "admin":
                    print("❌ Only admins can add students.")
                    continue
                name = input("Enter name: ")
                try:
                    age = int(input("Enter age: "))
                except ValueError:
                    print("❌ Invalid age.")
                    continue
                grade = input("Enter grade: ")
                student = Student(name, age, grade)
                self.db.add_student(student)
                print("✅ Student added.")

            elif choice == "2":
                students = self.db.get_students()
                if not students:
                    print("⚠️ No students found.")
                    continue
                table = [[s.id, s.name, s.age, s.grade] for s in students]
                print("\n--- Student List ---")
                print(tabulate(table, headers=["ID", "Name", "Age", "Grade"], tablefmt="grid"))

            elif choice == "3":
                if self.role != "admin":
                    print("❌ Only admins can update students.")
                    continue
                try:
                    sid = int(input("Enter Student ID to update: "))
                    name = input("New name: ")
                    age = int(input("New age: "))
                    grade = input("New grade: ")
                except ValueError:
                    print("❌ Invalid input.")
                    continue
                self.db.update_student(sid, name, age, grade)
                print("✅ Student updated.")

            elif choice == "4":
                if self.role != "admin":
                    print("❌ Only admins can delete students.")
                    continue
                try:
                    sid = int(input("Enter Student ID to delete: "))
                except ValueError:
                    print("❌ Invalid ID.")
                    continue
                self.db.delete_student(sid)
                print("✅ Student deleted.")

            elif choice == "5":
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid choice, try again.")

# === MAIN PROGRAM ===
if __name__ == "__main__":
    print("=== Welcome to Student Management System ===")

    # Ensure user table exists
    create_user_table()

    # Check if any user exists
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    conn.close()

    if user_count == 0:
        print("⚠️ No users found. Let's create the first admin account.")
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        add_user(username, password, "admin")
        print("✅ Admin account created. Please log in again.")

    # Login prompt
    username = input("Username: ")
    password = input("Password: ")
    role = login(username, password)

    if role is None:
        print("❌ Login failed. Exiting...")
        exit()

    print(f"✅ Logged in as '{username}' ({role})")

    # Start menu
    manager = StudentManager(role)
    manager.menu()