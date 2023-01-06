from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    fruit = ["apple", "banana", "cherry"]
    return render_template("index.html", list=fruit)
