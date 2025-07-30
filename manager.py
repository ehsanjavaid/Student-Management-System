from student import Student
from storage import save_to_file, file_load

class studentmanager:
    def __init__(self):
        self.students = []
    def file_load(self):
        self.students = file_load()

    def add_students(self):
        name = input("Enter the student")
        try:
            age = int(input("enter the student age "))
            marks = float(input("enter the student marks "))
            self.students.append(Student(name, age, marks))
            print("data added successfully")
        except ValueError:
            print("Invalid input ")

    def view_students(self):
        if not self.students:
            print("student not found")
        else:
            print("\n --- student list ---")
            for idx, s in enumerate(self.students, start=1):
                print(f"{idx}. Name: {s.name}, Age: {s.age}, Marks: {s.marks}")

    def search_students(self):
        student = input("Enter student name")
        found = [s for s in self.students if s.name.lower() == student.lower()]
        if found:
            for s in found:
                print(f"Found:  Name: {s.name}, Age: {s.age}, Marks: {s.marks}")
            else:
                print("Student not found")
    def create_student(self, name, age, marks):
        return Student(name, age, marks)
    
    def save_to_file(self):
        save_to_file(self.students)

