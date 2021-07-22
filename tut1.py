# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 13:09:11 2021

@author: jadec
"""

# python "C:/Users/jadec/OneDrive/Workspaces/pythonWorkspace/flask/tut1.py"

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    # return "Hello! this is my first flask app, the main page <h1>Hello World<h1>"


# @app.route("/<name>")
# def user(name):
#     return render_template("index.html", content=["tim", "john"])
#     # return f"Hello {name}!"

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!!"))

@app.route("/pricing/")
def pricing():
    return render_template("pricing.html")



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        # session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")



@app.route("/<usr>")
def user(usr):
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)