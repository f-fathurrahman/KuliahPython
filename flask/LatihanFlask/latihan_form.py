from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "This is my webpage"

@app.route("/simple_form", methods=["GET", "POST"])
def handle_simple_form():
    if request.method == "POST":
        username = request.form["nama"]
        return "Hello %s" % username
    return """
    You need to login first.
    <p>
    <a href="/login">Login here</a>
    </p>
    """

@app.route("/login")
def handle_login():
    return render_template("simple_form_v1.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

