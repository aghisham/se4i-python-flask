from app import app
from flask import Flask
from app.models.user import User


@app.route("/")
def homepage():
    return "hello from homepage"

@app.route("/about")
def about():
    return "about page is here"


@app.route("/get-name")
def get_name():
    user = User("SE4I project")

    return user.get_name()

