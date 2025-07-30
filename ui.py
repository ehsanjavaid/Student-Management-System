# ui.py
import tkinter as tk
from tkinter import messagebox
from manager import studentmanager

class StudentApp:
    def __init__(self, root):
        self.manager = studentmanager()
        self.manager.file_load()

        self.root = root
        self.root.title("Student Management System")

        # Input fields
        tk.Label(root, text="Name").grid(row=0, column=0)
        tk.Label(root, text="Age").grid(row=1, column=0)
        tk.Label(root, text="Marks").grid(row=2, column=0)

        self.name_entry = tk.Entry(root)
        self.age_entry = tk.Entry(root)
        self.marks_entry = tk.Entry(root)

        self.name_entry.grid(row=0, column=1)
        self.age_entry.grid(row=1, column=1)
        self.marks_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(root, text="Add Student", command=self.add_students).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="View Students", command=self.view_students).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="Search Student", command=self.search_students).grid(row=5, column=0, columnspan=2)
        tk.Button(root, text="Save & Exit", command=self.save_and_exit).grid(row=6, column=0, columnspan=2)

    def add_students(self):
        try:
            name = self.name_entry.get()
            age = int(self.age_entry.get())
            marks = float(self.marks_entry.get())
            self.manager.students.append(self.manager.create_student(name, age, marks))
            messagebox.showinfo("Success", "Student added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    def view_students(self):
        students = "\n".join([f"{s.name}, Age: {s.age}, Marks: {s.marks}" for s in self.manager.students])
        messagebox.showinfo("Student List", students if students else "No students found")

    def search_students(self):
        name = self.name_entry.get()
        found = [s for s in self.manager.students if s.name.lower() == name.lower()]
        if found:
            s = found[0]
            messagebox.showinfo("Found", f"{s.name}, Age: {s.age}, Marks: {s.marks}")
        else:
            messagebox.showerror("Error", "Student not found")

    def save_and_exit(self):
        self.manager.save_to_file()
        self.root.quit()

