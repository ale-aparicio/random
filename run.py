import os
import json
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

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


#Route for the Sub Theories connected to the MongoDB database
@app.route("/world_theories")
def world_theories():
    worlds = mongo.db.world.find()
    return render_template("world_theories.html", page_title="World Theories", worlds=worlds)

@app.route("/add_theories")
def add_theories():
    data = []
    with open("data/theories.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("add_theory.html", page_title="Add a Theory", theories=data)
#remember to change debug = true to false

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)

