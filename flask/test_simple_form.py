from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the index page"


@app.route("/success/<name>")
def success(name):
    return "Welcome %s" % name

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("success", name=user))
    else:
        user = request.args.get("nm")
        passwd = request.args.get("passwd")
        return "Please login first: " + user + " your passwd: " + passwd
        #return redirect(url_for("success", name=user))

if __name__ == "__main__":
    app.run(debug=True)





