import turtle

def donnees():
    nb_cote=int(input("veuillez saisir le nb de cotes:"))
    nb_rep=int(input("veuillez saisir le nb de rep:"))
    taille=int(input("veuillez saisir la taille du motif:"))
    angle=int(input("veuillez saisir l'angle de rotation entre les repetitions:"))
    couleur=input("veuillez saisir la couleur:")
    return nb_cote, nb_rep, taille, angle, couleur

def dessin():
    nb_cote, nb_rep, taille, angle, couleur=donnees()
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(100)
    angle_fig=360/nb_cote
    t.color(couleur)
    for i in range(nb_rep):
        for n in range(nb_cote):
            t.forward(taille)
            t.right(angle_fig)
        t.right(angle)
    turtle.done()

dessin()