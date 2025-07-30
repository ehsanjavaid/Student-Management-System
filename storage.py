import json
from student import Student
import os

FILE_NAME = "students.json"

def save_to_file(students):
    with open(FILE_NAME, "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=4)
    print("✅ Data saved successfully!")

def file_load():
    """Load students from JSON file safely"""
    if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
        return [] 

    with open(FILE_NAME, "r") as f:
        try:
            data = json.load(f)
            return [Student(d["name"], d["age"], d["marks"]) for d in data]
        except json.JSONDecodeError:
            return []
