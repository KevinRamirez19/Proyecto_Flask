from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola Mundo"
@app.route("/PGC/")
def PGC():
    return render_template("index.html")