# Contoh minimal Flask

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    response_str = """
    <html>

    <head>
    <title>This is a title</title>
    </head>

    <body>
    <h1>Hello MI3103.</h1>

    <p>My name is efefer.</p>

    <p>I am running via flask run</p>
    </body>

    </html>
    """
    return response_str

