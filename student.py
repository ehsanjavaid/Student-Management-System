class Student():
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'marks': self.marks
        }


    

    