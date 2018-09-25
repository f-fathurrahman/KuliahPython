from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Example of using template, passing dict"

@app.route("/result")
def show_result():
    res = {"phy": 50, "che":60, "maths":70}
    return render_template("exam_results.html", results=res)

if __name__ == "__main__":
    app.run(debug=True)




