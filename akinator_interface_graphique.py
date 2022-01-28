import pickle
from time import sleep
from fonctions_primaires import *
from tkinter import *

class Akinator():
    
    def __init__(self):
        with open("arbre_akinator.pik", "rb") as fichierArbre:
                self.arbre = pickle.load(fichierArbre)
        self.fenetre = Tk()  # Crée la fenêtre de jeu
        self.variable_texte = StringVar()
        self.creation_fenetre()
    
    def creation_fenetre(self):
        self.fenetre.title("Akinator")  # Ajoute un titre à la fenêtre
        self.fenetre.geometry("")  # Définit la taile de la fenêtre

        # Label
        label_question = Label(self.fenetre, textvariable=self.variable_texte)

        self.variable_texte.set("Bienvenue sur le jeu Akinator ! Clique sur le bouton \"Jouer\" pour commencer la partie !")
        label_question.grid(row=0, column=0, columnspan=2)

        # Boutons

        def jeu():
            """Lance le jeu en créant les boutons de réponse oui/non et modifiant la variable de texte pour la question
            """
            bouton_oui = Button(self.fenetre, text="oui", command= lambda: self.variable_texte.set("Oui"))
            bouton_non = Button(self.fenetre, text="non", command= lambda: self.variable_texte.set("Non"))
            bouton_oui.grid(row=1, column=0)
            bouton_non.grid(row=1, column=1)
            bouton_jouer.grid_remove()
            self.variable_texte.set("Pense à un animal.")
            self.fenetre.update()
            sleep(3)
            self.variable_texte.set(racine(self.arbre))

        bouton_jouer = Button(self.fenetre, text="Jouer", command= lambda: jeu())
        bouton_jouer.grid(row=1, column=0, columnspan=2)

        self.fenetre.mainloop()  # Lance la fenêtre
        
partie = Akinator()
