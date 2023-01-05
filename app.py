from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    x = "bob"
    return render_template("index.html", name=x)