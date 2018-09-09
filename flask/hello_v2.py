# Contoh minimal Flask

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    response_str = """
    Hello MI3103.

    My name is efefer.

    I am running via flask run
    """
    return response_str

