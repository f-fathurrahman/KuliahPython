from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Example of using template"

@app.route("/score/<int:score>")
def show_result(score):
    return render_template("marks.html", marks=score)


if __name__ == "__main__":
    app.run(debug=True)







