from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

FILEOUT = open("data.dat", "w")

@app.route("/", methods=["POST", "GET"])
def handle_index():
    rec_data = request.args.get("data")
    if rec_data:
        FILEOUT.write("%s %s\n" % (datetime.now(), rec_data))
        FILEOUT.flush()
    return "Hello, I am waiting for data"

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
