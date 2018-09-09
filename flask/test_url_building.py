from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the index page"

@app.route("/login")
def login():
    return "This is the login page"

@app.route("/user/<username>")
def profile(username):
    return "This is {}'s profile".format(username)

with app.test_request_context():
    print("URL for index is: ", url_for("index"))
    print("URL for login is: ", url_for("login"))
    print("URL for login with next is: ", url_for("login", next="/"))
    print("URL for profile is: ", url_for("profile", username="John Doe"))


