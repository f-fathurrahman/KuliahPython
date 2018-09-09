from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def handle_root():
    if request.method == "POST":
        return "This is the handler for POST"
    else:
        return "This is the handler for GET"


