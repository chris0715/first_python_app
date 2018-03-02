from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        new_student_id = request.form.get("studendt-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")
        return redirect(url_for("studendts_page"))
    return "Hello World!"
