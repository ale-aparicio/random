import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

#Route for the Explore page connected to the respective Json data page
@app.route("/explore")
def explore():
        data = []
        with open("data/explore.json", "r") as json_data:
            data = json.load(json_data)
        return render_template("explore.html", page_title="Explore", explore=data)


@app.route("/media")
def media():
    return render_template("media.html", page_title="Media")

#Route for the Theories page connected to the respective Json data page
@app.route("/theories")
def theories():
    data = []
    with open("data/theories.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("theories.html", page_title="Theory", theories=data)


#Route for the Sub Theories Connected to the sub-theories.json page 
@app.route("/theories/<theories_url>")
def theories_content(theory):
    return render_template("<theories_url>", page_title="<theories_title>", theories=theory)


@app.route("/world_theories")
def world_theories():
    return render_template("world_theories.html", page_title="World Theories")

@app.route("/character_theories")
def character_theories():
    return render_template("character_theories.html", page_title="Character Theories")


#remember to change debug = true to false

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

