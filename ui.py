import tkinter as tk
from tkinter import ttk, messagebox
from manager import studentmanager
from student import Student


class StudentApp:
    def __init__(self, root):
        self.manager = studentmanager()
        self.manager.file_load()

        # Input fields
        self.entry_name = tk.Entry(root)
        self.entry_name.pack()
        
        self.entry_age = tk.Entry(root)
        self.entry_age.pack()
        
        self.entry_grade = tk.Entry(root)
        self.entry_grade.pack()

        # Add button
        self.add_button = tk.Button(root, text="Add Student", command=self.on_add_button)
        self.add_button.pack()

        # Table
        self.tree = ttk.Treeview(root, columns=("Name", "Age", "Grade"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Grade", text="Grade")
        self.tree.pack()

        self.refresh_table()

    def on_add_button(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        grade = self.entry_grade.get()

        self.manager.add_student(Student(name, age, grade))
        self.refresh_table()

    def refresh_table(self):
        # Clear table
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Get fresh data from DB
        students = self.manager.get_students()
        for student in students:
            self.tree.insert("", "end", values=(student.name, student.age, student.grade))

