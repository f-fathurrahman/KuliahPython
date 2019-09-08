from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "This is a homepage"

@app.route("/contoh-gambar")
def contoh_gambar():
    return render_template("example_image.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
