from flask import Flask, session, request, url_for, redirect

app = Flask(__name__)

app.secret_key = "This is secret"

@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        return "You are logged in as " + username + "<br>" + \
               "<b><a href='/logout'>Click here to log out</a></b>"
    
    return """
    You are not logged in <br>
    <b>
    <a href='/login'>Click here to log in</a>
    </b>
    """

@app.route("/login", methods=["GET", "POST"])
def handle_login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect( url_for("index") )
    #
    return """
    <form action="", method="POST">
      <p><input type="text" name="username" /></p>
      <p><input type="submit" value="Login" /></p>
    </form>
    """

@app.route("/logout")
def handle_logout():
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)


