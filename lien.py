from flask import Flask, render_template, request, url_for
import subprocess
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/generer", methods=["POST"])
def generer():
    print("fonctionne")
    nb_cotes = request.form["cotes"]
    nb_rep = request.form["rep"]
    taille = request.form["taille"]
    angle = request.form["angle"]
    couleur = request.form["couleur"]
    subprocess.run(["python3", "generateur.py", nb_cotes, nb_rep, taille, angle, couleur])
    image_url = url_for('static', filename='motif.png')
    return render_template("index.html", message="Motif généré !", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
