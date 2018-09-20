from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", date_now=datetime.datetime.now())


@app.route("/about-me")
def about_me():
    return """
    My name is Jono.<br>
    I am a student of MI3103"<br>
    I am learning web development using Flask.<br>
    """

