
class Student:
    
    school_name =  "Springifeld Elementary"

    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id
        # students.append(self)

    def __str__(self):
        return "Student"

    def get_name_capitalized(self):
        return self.name.capitalize()
