from app import app
from flask import Flask
from app.models.project import Project


@app.route("/")
def homepage():
    return "hello from homepage", 418

@app.route("/about")
def about():
    return "about page is here"


@app.route("/get-name")
def get_name():
    project = Project("SE4I project")

    return project.get_name()

