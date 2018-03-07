from flask import Flask, render_template, redirect, url_for, request
from Student import Student

students = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        new_student_id = request.form.get("studendt-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")
        new_student = Student(new_student_name, new_student_last_name)
        students.append(new_student)
        return redirect(url_for("hello"))
    
    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)