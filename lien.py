from flask import Flask, render_template, request, url_for #librairie flask pour gerer le serveur web avec render_template pour l'affichage et url_for pour fournir les url necessaire au cade html
import subprocess #librairie pour compiler le deuxieme fichier python sans perturber le serveur 
import atexit
import os

images_genere=0
image_affiche=0

app = Flask(__name__) #creation de l'application flask

def on_shutdown():
    print("Le serveur s'arrête, exécution du programme...")
    global images_genere
    for i in range(images_genere + 1):
        try:
            os.remove(f"static/motif{i}.eps")
            os.remove(f"static/motif{i}.png")
        except FileNotFoundError:
            print(f"Fichier motif{i} manquant, ignoré.")

atexit.register(on_shutdown)


@app.route("/") #lorsque l'on se connecte sur la page par defaut 
def index():
    return render_template('index.html') #afficher le code html et css


@app.route("/generer", methods=["POST"]) #losque l'on clique sur generer on lance la methode post presente dans le form identifier comme /generer
def generer():
    global images_genere, image_affiche
    images_genere+=1
    image_affiche= images_genere
    mode = request.form["mode"]
    if mode == "forme":
        nb_cotes = request.form["cotes"] #recupere la donnee cotes
        if not nb_cotes:
            nb_cotes = str(3)  # valeur par défaut
        nb_rep = request.form["rep"]
        if not nb_rep:
            nb_rep = str(3)
        taille = request.form["taille"]
        angle = request.form["angle"]
        if not angle:
            angle = str(15)
        couleur = request.form["couleur"]
        subprocess.run(["python3", "generateur.py",mode, str(images_genere), nb_cotes, nb_rep, taille, angle, couleur], check=True) 
    elif mode == "fractale":
        taille = request.form["taille"]
        niveau = request.form["niveau"]
        if not niveau:
            niveau = str(3)
        couleur = request.form["couleur"]
        subprocess.run(["python3", "generateur.py",mode, str(images_genere), taille, niveau, couleur], check=True) 
    elif mode == "spirale":
        taille = request.form["taille"]
        angle = request.form["angle"]
        if not angle:
            angle = str(15)
        pas = request.form["pas"]
        if not pas:
            pas = str(0.5)
        couleur = request.form["couleur"]
        subprocess.run(["python3", "generateur.py",mode, str(images_genere), taille, angle, pas, couleur], check=True) 
    image_url = url_for('static', filename=f'motif{images_genere}.png') 
    return render_template("index.html", image_url=image_url) #affiche la page avec l'image genere 

@app.route("/precedent", methods=["POST"])
def precedent():
    global image_affiche
    if image_affiche-1>=1:
        image_affiche-=1
    image_url = url_for('static', filename=f'motif{image_affiche}.png') 
    return render_template("index.html", image_url=image_url)

@app.route("/suivant", methods=["POST"])
def suivant():
    global images_genere, image_affiche
    if image_affiche+1 <= images_genere:
        image_affiche+=1
    image_url = url_for('static', filename=f'motif{image_affiche}.png') 
    return render_template("index.html", image_url=image_url)


app.run(debug=True) #demare le serveur et le met a jour a la moindre modifictaion du code 
