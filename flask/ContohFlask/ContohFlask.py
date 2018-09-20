from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello ..."


@app.route("/about-me")
def about_me():
    return """
    My name is Jono.<br>
    I am a student of MI3103"<br>
    I am learning web development using Flask.<br>
    """

