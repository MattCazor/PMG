import turtle 
import sys #librairie for permettre un fonctionnement en backend
from PIL import Image 
import math

screen = turtle.Screen() 
t = turtle.Turtle()
t.speed(0)
turtle.tracer(0, 0) 

def enregistrement(image_genere):
    screen.update()
    canvas = screen.getcanvas() #recupere le dessin
    eps_path = f"static/motif{image_genere}.eps" #indique ou sauvgearder le fichier .eps
    png_path = f"static/motif{image_genere}.png" #indique ou sauvegarder le fichier .png
    canvas.postscript(file=eps_path) #enregistrement du dessin 
    img = Image.open(eps_path) #recupere le dessin dans une variable sous forme d'image 
    img.save(png_path) #sauvegarde l'image en .png
    turtle.bye() #ferme la console de dessin 


def dessin(image_genere, cote, rep, taille, angle, couleur):
    angle_fig=360/cote 
    t.color(couleur)
    for i in range(rep): 
        for n in range(cote): 
            t.forward(taille)
            t.right(angle_fig)
        t.right(angle)
    enregistrement(image_genere)
    
def fractale(longueur, niveau):
    if niveau == 0:
        t.forward(longueur)
    else:
        longueur /= 3
        fractale(longueur, niveau - 1)
        t.left(60)
        fractale(longueur, niveau - 1)
        t.right(120)
        fractale(longueur, niveau - 1)
        t.left(60)
        fractale(longueur, niveau - 1)

def dessine_fractale(image_genere, taille, niveau, couleur):
    t.color(couleur)
    t.penup()        
    t.goto(-taille/2, taille/3)      
    t.pendown()       
    print(niveau)

    for i in range(3):  
        fractale(taille, niveau)
        t.right(120)
    enregistrement(image_genere)

def spirale(image_genere, taille, angle, pas, couleur):
    t.color(couleur)
    longueur = 1
    while True:
        t.forward(longueur)
        t.right(angle)
        longueur += pas
    
        x, y = t.pos() #recupere la position du curseur 
        rayon = math.hypot(x, y) #calcul la distance entre le centre et la position du curseur 
        if rayon * 2 >= taille:
            break
    enregistrement(image_genere)

mode = sys.argv[1] #recupere la donee fournie par flask 
if mode == "forme":
    image_genere = int(sys.argv[2]) 
    nb_cote = int(sys.argv[3]) 
    nb_rep = int(sys.argv[4]) 
    taille = int(sys.argv[5]) 
    angle = int(sys.argv[6])
    couleur = sys.argv[7] 
    dessin(image_genere, nb_cote, nb_rep, taille, angle, couleur)
elif mode=="fractale":
    image_genere = int(sys.argv[2])
    taille = int(sys.argv[3]) 
    niveau = int(sys.argv[4]) 
    couleur = sys.argv[5]
    dessine_fractale(image_genere, taille, niveau, couleur)
elif mode == "spirale":
    image_genere = int(sys.argv[2])
    taille = int(sys.argv[3])
    angle = int(sys.argv[4])
    pas = float(sys.argv[5])
    couleur = sys.argv[6]
    spirale(image_genere, taille, angle, pas, couleur)
