from tkinter import *
from turtle import *
import time, sys

#Fenètre Aventure
image = ""
TopLeft = ""
titre = ""
TopRight = ""
gauche = ""
centre = ""
droite = ""
BotLeft = ""
Bas = ""
BotRight = ""

def display(image, scale, couleur, TopLeft, title, TopRight, gauche, centre, droite, BotLeft, Bas, BotRight):
    if (image):
        root = Tk()
        if (couleur):
            couleur = couleur
        else:
            couleur = '#16e116' #Green
        root.configure(background=couleur)#filtre couleur
        root.title('World-War-III')
        if (scale):
            scale = scale
        else:
            scale = '510x345'
        root.geometry(scale)
        photo = PhotoImage(file=image)#Image arrière plan
        w = Label(root, image=photo)        
        #Title
        if (titre):
            text = Label(root, text=titre)
            w.grid(row=3, column=3)
            text.grid(row=2, column=3)
        #Haut Gauche
        if (TopLeft):
            text = Label(root, text=TopLeft)
            w.grid(row=3, column=3)
            text.grid(row=2, column=2)
        #Haut Droite
        if (TopRight):
            text = Label(root, text=TopRight)
            w.grid(row=3, column=3)
            text.grid(row=2, column=4)
        #Centr Gauche
        if (gauche):
            text = Label(root, text=gauche)
            w.grid(row=3, column=3)
            text.grid(row=3, column=2)
        #Centre
        if (centre):
            text = Label(root, text=centre)
            w.grid(row=3, column=3)
            text.grid(row=3, column=3)
        #Centre Droite
        if (droite):
            text = Label(root, text=droite)
            w.grid(row=3, column=3)
            text.grid(row=3, column=4)
        #Bas Gauche
        if (BotLeft):
            text = Label(root, text=BotLeft)
            w.grid(row=3, column=3)
            text.grid(row=4, column=2)
        #Bas
        if (Bas):
            text = Label(root, text=Bas)
            w.grid(row=3, column=3)
            text.grid(row=4, column=3)
        #Bas Droite
        if (BotRight):
            text = Label(root, text=BotRight)
            w.grid(row=3, column=3)
            text.grid(row=4, column=4)
        #w.pack()
        root.mainloop()

new = 1
while(new == 1):
    
    #Ecran Titre
    image = 'world-war-3.png'
    scale = '510x345'
    couleur = '#16e116'
    titre = "Hello end of World!"
    gauche = "Options\nA) New\nB) load\nC) Save\nD) Info\nE) Quit"
    centre = "START\nCommencer une partie."
    display(image, scale, couleur, TopLeft, title, TopRight, gauche, centre, droite, BotLeft, Bas, BotRight)

    cmd = 1
    while(cmd == 1):
        print(centre,"\n")
        print(gauche,"\n")
        key = input("> ?")
        if key.upper() == "B":
            print("Charger une Partie.\nCette commande reste a venir.\n ")

        if key.upper() == "C":
            print("Sauvegardez une Partie.\nCette commande reste a venir.\n ")

        if key.upper() == "D":
            print("Informations Tutoriel.\nRépondez aux Questions avec des choix de réponse A,B,C,D,E\nOu inscrivez vous méme au clavier OUI,NON\n ")

        if key.upper() == "E":
            print("Fermeture du système...\nBye bye!")
            new = 0
            cmd = 0
            break

        if (key.upper() == "A" or key == ""):
            print("Nouvelle Partie.\n ")

            #Display New Game
            image = 'world-war-4.png'
            titre = "WORLD WAR III"
            gauche = "Tactic\nA) Fuir\nB) Cacher\nC) Piller\nD) Pleur\nE) Suicide"
            centre = "La Terre Tremble sous l'impacte des Bombes!\nQu'allez-vous faire en premier\nFaite un Choix."
            droite = "DANGER!\nTank\nHelico\nDrone\nSoldat\nStelite"
            display(image, scale, couleur, TopLeft, title, TopRight, gauche, centre, droite, BotLeft, Bas, BotRight)

            print(centre,"\n")
            print(gauche,"\n")
            key = input("> ?")
            if key.upper() == "":
                print("Vous ne savez pas?")
                key = input("[Oui/Non]")
                print("Ya, whatever...")
            print("L'instint de Survie Dit: Pas question vous devez COMBATRE!\n ")
            key = ""
            #CONTINU...

            image = 'world-war-4.png'
            titre = "WORLD WAR III"
            gauche = "Tactic\nUtiliser\nvos\nennemi\ncontre\nautre"
            centre = "Les ennemis s'avance vers vous.\nQu'allez-vous faire globalement?\nVoire ca."
            droite = "DANGER!\nTank\nHelico\nDrone\nSoldat\nStelite"
            display(image, scale, couleur, TopLeft, title, TopRight, gauche, centre, droite, BotLeft, Bas, BotRight)

            print(centre,"\n")
            print(gauche,"\n")
            key = input("> ?")
            if key.upper() == "":
                print("Vous ne savez TOUJOURS pas?")
                key = input("[Non]")
                print("Je vais vous dire comment faire.")
            print("Primo.Vous piratez le satelite. Les cibles désigné change pour la plus proche a droite. Le Soldat attaque le Drone attaque l'Hélico attaque le Tank attaque au missil sol/space le Satelite qui attaque les Soldats de ses rayon de la mort...\nBoom! Tout les ennemis sont mort et vous êtes seul a gagné!")
            key = ""
