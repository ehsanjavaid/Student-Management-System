from student import Student
from database import DatabaseManager
from tabulate import tabulate


class studentmanager:
    def __init__(self):
        self.db = DatabaseManager()

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
                self.db.add_student(student)
                print("✅ Student added.")

            elif choice == "2":
                students = self.db.get_students()
                table = [[s.id, s.name, s.age, s.grade] for s in students]
                print("\n--- Student List ---")
                print(tabulate(table, headers=[
                      "ID", "Name", "Age", "Grade"], tablefmt="grid"))

            elif choice == "3":
                sid = int(input("Enter Student ID to update: "))
                name = input("New name: ")
                age = int(input("New age: "))
                grade = input("New grade: ")
                self.db.update_student(sid, name, age, grade)
                print("✅ Student updated.")

            elif choice == "4":
                sid = int(input("Enter Student ID to delete: "))
                self.db.delete_student(sid)
                print("✅ Student deleted.")

            elif choice == "5":
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    manager = studentmanager()
    manager.menu()
