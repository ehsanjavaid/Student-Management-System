import tkinter as tk
from tkinter import ttk, messagebox
from manager import studentmanager
from student import Student 


class StudentApp:
    def __init__(self, root):
        self.manager = studentmanager()
        self.manager.file_load()

        self.root = root
        self.root.title("📚 Student Management System")
        self.root.geometry("600x400")
        self.root.config(bg="#f4f4f4")

        # ---- Title ----
        title_label = tk.Label(root, text="Student Management System",
                               font=("Arial", 16, "bold"), bg="#f4f4f4", fg="#333")
        title_label.pack(pady=10)

        # ---- Input Frame ----
        input_frame = tk.Frame(root, bg="#f4f4f4")
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="Name:", font=("Arial", 12),
                 bg="#f4f4f4").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(input_frame, text="Age:", font=("Arial", 12),
                 bg="#f4f4f4").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(input_frame, text="Marks:", font=("Arial", 12),
                 bg="#f4f4f4").grid(row=2, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.age_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.marks_entry = tk.Entry(input_frame, font=("Arial", 12))

        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)
        self.marks_entry.grid(row=2, column=1, padx=5, pady=5)

        # ---- Button Frame ----
        btn_frame = tk.Frame(root, bg="#f4f4f4")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Student", command=self.add_students,
                  font=("Arial", 12), bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Search Student", command=self.search_students,
                  font=("Arial", 12), bg="#2196F3", fg="white", width=15).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Save & Exit", command=self.save_and_exit,
                  font=("Arial", 12), bg="#f44336", fg="white", width=15).grid(row=0, column=2, padx=5)
        # tk.Button(btn_frame, text="Edit Student", command=self.edit_student,
        #           font=("Arial", 12), bg="#FF9800", fg="white", width=15).grid(row=1, column=0, padx=5, pady=5)

        # tk.Button(btn_frame, text="Delete Student", command=self.delete_student,
        #           font=("Arial", 12), bg="#E91E63", fg="white", width=15).grid(row=1, column=1, padx=5, pady=5)

        # ---- Table for Viewing Students ----
        self.tree = ttk.Treeview(root, columns=(
            "Name", "Age", "Marks"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Marks", text="Marks")
        self.tree.pack(fill="both", expand=True, pady=10)

        self.refresh_table()

    def refresh_table(self, students_list=None):
        """Refresh table with only given students"""
        for row in self.tree.get_children():
            self.tree.delete(row)

        if students_list:
            for s in students_list:
                self.tree.insert("", "end", values=(s.name, s.age, s.marks))

    def add_students(self):
        try:
            name = self.name_entry.get().strip()
            age = int(self.age_entry.get())
            marks = float(self.marks_entry.get())

            if not name:
                messagebox.showerror("Error", "Name cannot be empty!")
                return

            self.manager.students.append(Student(name, age, marks))
            self.refresh_table()
            messagebox.showinfo("Success", "Student added successfully!")

            # Clear input fields
            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.marks_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Invalid age or marks!")

    def search_students(self):
        name = self.name_entry.get().strip()
        found = [s for s in self.manager.students if s.name.lower() ==
                 name.lower()]
        if found:
            s = found[0]
            messagebox.showinfo(
                "Found", f"{s.name}, Age: {s.age}, Marks: {s.marks}")
        else:
            messagebox.showerror("Error", "Student not found")

    def save_and_exit(self):
        self.manager.save_to_file()
        self.root.quit()
