from flask import Flask, render_template, request, url_for #librairie flask pour gerer le serveur web avec render_template pour l'affichage et url_for pour fournir les url necessaire au cade html
import subprocess #librairie pour compiler le deuxieme fichier python sans perturber le serveur 

app = Flask(__name__) #creation de l'application flask

@app.route("/") #lorsque l'on se connecte sur la page par defaut 
def index():
    return render_template('index.html') #afficher le code html et css

@app.route("/generer", methods=["POST"]) #losque l'on clique sur generer on lance la methode post presente dans le form identifier comme /generer
def generer():
    nb_cotes = request.form["cotes"] #recupere la donnee cotes
    nb_rep = request.form["rep"]
    taille = request.form["taille"]
    angle = request.form["angle"]
    couleur = request.form["couleur"]
    subprocess.run(["python3", "generateur.py", nb_cotes, nb_rep, taille, angle, couleur]) #compile l'autre fichier python avec les donnees recuperer mais sans perturber le serveur 
    image_url = url_for('static', filename='motif.png') #recupere l'url de l'image cree 
    return render_template("index.html", image_url=image_url) #affiche la page avec l'image genere 

if __name__ == "__main__": #ne compile que si le fichier est compile directement 
    app.run(debug=True) #demare le serveur et le met a jour a la moindre modifictaion du code 
