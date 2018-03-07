
class Student:
    
    school_name =  "Springifeld Elementary"
    id = 1

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.id = 1

    def __str__(self):
        return "Student"

    def get_name_capitalized(self):
        return self.name.capitalize()
