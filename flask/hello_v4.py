# Contoh minimal Flask

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_page():
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

@app.route("/about")
def about_page():
    response_str = """
<html>
<title>
<head>About this site</head>
</title>

<body>

<p>This site is made using Flask.</p>

<p style="text-align: center;">&copy efefer 2018</p>
</body>

</html>
    """
    return response_str

