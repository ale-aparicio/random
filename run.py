import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/explore")
def explore():
    return render_template("explore.html")


@app.route("/media")
def explore():
    return render_template("media.html")


@app.route("/theories")
def explore():
    return render_template("theories.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)