import turtle 
import sys #librairie for permettre un fonctionnement en backend
from PIL import Image 
import math

screen = turtle.Screen() 
t = turtle.Turtle()
t.speed(0)
turtle.tracer(0, 0) 

def enregistrement():
    screen.update()
    canvas = screen.getcanvas() #recupere le dessin
    eps_path = "static/motif.eps" #indique ou sauvgearder le fichier .eps
    png_path = "static/motif.png" #indique ou sauvegarder le fichier .png
    canvas.postscript(file=eps_path) #enregistrement du dessin 
    img = Image.open(eps_path) #recupere le dessin dans une variable sous forme d'image 
    img.save(png_path) #sauvegarde l'image en .png
    turtle.bye() #ferme la console de dessin 


def dessin(cote, rep, taille, angle, couleur):
    angle_fig=360/cote 
    t.color(couleur)
    for i in range(rep): 
        for n in range(cote): 
            t.forward(taille)
            t.right(angle_fig)
        t.right(angle)
    enregistrement()
    
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

def dessine_fractale(taille, niveau, couleur):
    t.color(couleur)
    t.penup()        
    t.goto(-taille/2, taille/3)      
    t.pendown()       

    for i in range(3):  
        fractale(taille, niveau)
        t.right(120)
    enregistrement()

def spirale(taille, angle, pas, couleur):
    t.color(couleur)
    longueur = 1
    while True:
        t.forward(longueur)
        t.right(angle)
        longueur += pas
    
        x, y = t.pos()
        diametre = math.hypot(x, y)
        if diametre * 2 >= taille:
            break
    enregistrement()

mode = sys.argv[1]
if mode == "forme":
    nb_cote = int(sys.argv[2]) 
    nb_rep = int(sys.argv[3]) 
    taille = int(sys.argv[4]) 
    angle = int(sys.argv[5])
    couleur = sys.argv[6] 
    dessin(nb_cote, nb_rep, taille, angle, couleur)
elif mode=="fractale":
    taille = int(sys.argv[2]) 
    niveau = int(sys.argv[3]) 
    couleur = sys.argv[4]
    dessine_fractale(taille, niveau, couleur)
elif mode == "spirale":
    taille = int(sys.argv[2])
    angle = int(sys.argv[3])
    pas = float(sys.argv[4])
    couleur = sys.argv[5]
    spirale(taille, angle, pas, couleur)
