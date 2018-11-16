from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {"username" : "Fathurrahman"}
    posts = [
        {
            "author": {"username": "Fadjar"},
            "body": "Hello from Fadjar"
        },
        {
            "author": {"username": "ffr"},
            "body": "Hello from ffr"
        }
    ]
    #
    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route("/index-v2")
def index_v2():
    user = {"username" : "Fathurrahman"}
    return render_template("index.html", user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me = {}".format(
              form.username.data, form.remember_me.data))
        return redirect("/index")
    return render_template("login.html", title="Sign In", form=form)
