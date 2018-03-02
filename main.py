from Student import Student

students = []

def get_students_titlecase():
    for student in students:
        print(student["name"])

def add_student (name, id=12):
    stu_obj = {"name": name, "student_id": id}
    students.append(stu_obj)

def save_files(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
    except Exception:
        print("there was an error")


def read_files():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read the file")

read_files()

student_name = input("enter student name ")
student_id = input("enter his id ")

add_student(student_name)
save_files(student_name)
print()