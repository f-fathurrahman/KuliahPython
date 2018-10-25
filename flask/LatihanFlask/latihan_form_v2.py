from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("simple_form_v2.html")

@app.route("/result", methods=["POST", "GET"])
def handle_result():
    if request.method == "POST":
        return """
        <p> Nama: %s </p>
        <p> Nilai matematika: %s </p>
        <p> Nilai fisika: %s </p>
        <p> Nilai kimia: %s </p>
        """ % ( request.form["nama"],
                request.form["matematika"],
                request.form["fisika"],
                request.form["kimia"]
        )
    #
    return "Silakan masukkan data dulu<br>Klik di sini untuk memasukkan data"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


