from flask import Flask, render_template, redirect, request




app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/developer")
def developer():
    return render_template("developer.html")