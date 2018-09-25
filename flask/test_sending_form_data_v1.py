from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def show_entry_student_scores():
    return render_template("entry_student_scores.html")

@app.route("/result", methods=["GET", "POST"])
def show_results():
    if request.method == "POST":
        res = request.form
        return render_template("exam_results.html", results=res)
    else:
        return redirect(url_for("show_entry_student_scores"))

if __name__ == "__main__":
    app.run(debug=True)


