from flask import Flask, request
import datetime

print(__name__)
app = Flask(__name__)

@app.route("/process-data")
def handle_process():
    nama = request.args.get("nama")
    makanan = request.args.get("makanan")
    minuman = request.args.get("minuman")
    ret_str = """
    Detail pesanan<br>
    Nama    : %s <br>
    Makanan : %s <br>
    Minuman : %s <br>

    Pesanan Anda telah diterima pada %s
    """ % (nama, makanan, minuman, datetime.datetime.now())
    return ret_str

if __name__ == "__main__":
    app.run(debug=True)
