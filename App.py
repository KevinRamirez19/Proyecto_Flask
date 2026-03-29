from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola Mundo"
@app.route("/Prueba/")
def Prueba():
    return render_template("index.html")
@app.route("/index/")
def cluster():
    info = Clustering.RealizarClustering()

    return render_template(
        "ClusterResult.html",
        resultado=info["resultados"],
        centroides=info["centroides"],
        resumenClusters=info["resumenClusters"]
    )
@app.route("/PGC/")
def PGC():
    return render_template("PGC.html")