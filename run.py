import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/explore")
def explore():
        data = []
        with open("data/explore.json", "r") as json_data:
            data = json.load(json_data)
        return render_template("explore.html", page_title="Explore", explore=data)


@app.route("/media")
def media():
    return render_template("media.html")


@app.route("/theories")
def theories():
    return render_template("theories.html")


#remember to change debug = true to false
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

