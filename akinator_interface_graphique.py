from tkinter import *


# Création de la fenêtre
fenetre = Tk()  # Crée la fenêtre de jeu
fenetre.title("Akinator")  # Ajoute un titre à la fenêtre
fenetre.geometry("")  # Définit la taile de la fenêtre

# Label
variable_texte = StringVar()
label_question = Label(fenetre, textvariable=variable_texte)

variable_texte.set("Heyo")
label_question.pack()

fenetre.mainloop()  # Lance la fenêtre