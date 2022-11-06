from flask import Flask
from flask import render_template
from flask import request
from PIL import Image

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/upload", methods=["post"])
def upload():
    file = request.files["uploadfile"]
    img = Image.open(file)
    return "Hello Upload"


if __name__ == "__main__":
    app.run(debug=True)
