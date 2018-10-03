from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("test_cookies_v1.html")


@app.route("/setcookie", methods=["POST"])
def set_cookie():
    userID = request.form["userID"]
    resp = make_response( render_template("read_cookie_v1.html") )
    resp.set_cookie("userID", userID)
    return resp


@app.route("/getcookie")
def get_cookie():
    userID = request.cookies.get("userID")
    return "<h1>Welcome " + userID + "</h1>"

if __name__ == "__main__":
    app.run(debug=True)


