from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def home():
    return "Hola Mundos"