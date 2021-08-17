import os
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    data = []
    with open("data/theories.json", "r") as json_data:
        data = json.load(json_data)
    return render_template(
        "index.html",
        theories=data
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


# Route for the Theories page connected to the respective Json data page


@app.route("/theories")
def theories():
    data = []
    with open("data/theories.json", "r") as json_data:
        data = json.load(json_data)
    return render_template(
        "theories.html",
        page_title="Theory",
        theories=data
    )


# Route for the Sub Theories connected to the MongoDB database


@app.route("/world_theories")
def world_theories():
    worlds = mongo.db.world.find()
    return render_template(
        "world_theories.html",
        page_title="World Theories",
        worlds=worlds
        )


# Function to add a theory


@app.route("/add_theories", methods=["GET", "POST"])
def add_theories():
    if request.method == "POST":
        # Insert a theory linked to the world_theory category
        world = {
            "title": request.form.get("title"),
            "user": request.form.get("user"),
            "content": request.form.get("content")
        }
        mongo.db.world.insert_one(world)
        # Message when Theory has been sucessfully added
        flash("Theory Sucessfully Added")
    # Route for the categories selection into the theories.json
    data = []
    with open("data/theories.json", "r") as json_data:
        data = json.load(json_data)
    return render_template(
        "add_theory.html", page_title="Create a Theory",
        theories=data)


# Function to edit a theory


@app.route("/edit_theories/<theory_id>", methods=["GET", "POST"])
def edit_theories(theory_id):
    if request.method == "POST":
        # Update theory linked to the world_theory category
        world_edit = {
            "title": request.form.get("title"),
            "user": request.form.get("user"),
            "content": request.form.get("content")
        }
        # Message when Theory has been sucessfully added
        flash("Theory Sucessfully Added")

    world = mongo.db.world.find_one({"_id": ObjectId(theory_id)})
    data = []
    with open("data/theories.json", "r") as json_data:
        data = json.load(json_data)
    return render_template(
        "edit_theory.html",
        page_title="Edit a Theory",
        world=world,
        theories=data
    )


# remember to change debug = true to false


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
        )
