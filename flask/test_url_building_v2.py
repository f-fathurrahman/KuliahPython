from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is an example for URL building"

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello %s" % name

@app.route("/blog/<int:postID>")
def show_blog(postID):
    return "This is blog number %d" % postID

@app.route("/float/<float:x>")
def show_float(x):
    return "This is float number %f" % x

@app.route("/path/<path:pth>")
def show_route(pth):
    print("pth = ", pth)
    print("type(pth) = ", type(pth))
    return "This is the path: %s" % pth


if __name__ == "__main__":
    app.run()
