from sqlite3 import Row
from tkinter import *

# Création de la fenêtre
fenetre = Tk()  # Crée la fenêtre de jeu
fenetre.title("Akinator")  # Ajoute un titre à la fenêtre
fenetre.geometry("")  # Définit la taile de la fenêtre

# Label
variable_texte = StringVar()
label_question = Label(fenetre, textvariable=variable_texte)

variable_texte.set("Bienvenue sur le jeu Akinator ! Clique sur le bouton \"Jouer\" pour commencer la partie !")
label_question.grid(row=0, column=0, columnspan=2)

# Boutons

def jeu():
    bouton_oui = Button(fenetre, text="oui", command= lambda: variable_texte.set("Oui"))
    bouton_non = Button(fenetre, text="non", command= lambda: variable_texte.set("Non"))
    bouton_oui.grid(row=1, column=0)
    bouton_non.grid(row=1, column=1)
    bouton_jouer.grid_remove()
    variable_texte.set("Le jeu peut commencer !")

bouton_jouer = Button(fenetre, text="Jouer", command= lambda: jeu())
bouton_jouer.grid(row=1, column=0, columnspan=2)

fenetre.mainloop()  # Lance la fenêtre