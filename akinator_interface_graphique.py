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
        self.etape_resultat = 0 # Permet de savoir où nous sommes dans l'étape de résultat
        self.stock_animal_attendu = "" # Variable qui stockera l'animal et la question donnée par l'utilisateur
        self.creation_fenetre()
    
    
    def creation_fenetre(self):
        self.fenetre.title("Akinator")  # Ajoute un titre à la fenêtre
        self.fenetre.geometry("500x500")  # Définit la taile de la fenêtre

        # Label, mise en place du label où se trouvera les messages d'Akinator
        label_question = Label(self.fenetre, textvariable=self.variable_texte)
        self.variable_texte.set("Bienvenue sur le jeu Akinator ! Clique sur le bouton \"Jouer\" pour commencer la partie !")
        label_question.grid(row=0, column=0, columnspan=2)

        # Bouton jouer, qui permet de lancer une partie
        bouton_jouer = Button(self.fenetre, text="Jouer", command= lambda: self.lancement_jeu(bouton_jouer))
        bouton_jouer.grid(row=1, column=0, columnspan=2)

        self.fenetre.mainloop()  # Lance la fenêtre
    
    
    def lancement_jeu(self, bouton_a_retirer = None):
        """Lance le jeu en créant les boutons de réponse oui/non et modifiant la variable de texte pour la question
        """
        #* Définit l'entrée utilisateur et le bouton pour envoyer la réponse
        entree_utilisateur = Entry(self.fenetre, width=30)
        bouton_envoi = Button(self.fenetre, text="Envoyer la réponse", command= lambda: self.gestion_jeu(entree_utilisateur))
        
        #* Les places dans la fenêtre
        entree_utilisateur.grid(row=1, column=0)
        bouton_envoi.grid(row=1, column=1)
        if bouton_a_retirer is not None: # Retire le bouton jouer s'il est existant
            bouton_a_retirer.grid_remove()
            
        #* Initialise le début du jeu
        self.variable_texte.set("Pense à un animal.")
        self.fenetre.update()
        sleep(1)
        self.variable_texte.set(racine(self.arbre))
    
    
    def gestion_jeu(self, entree):
        """Fonction gérant le déroulé du jeu en fonction des réponses du joueur"""
        #* Récupère la réponse du joueur et supprime l'entrée utilisateur
        reponse = entree.get()
        entree.delete(0, END)
        
        #* Si jamais l'arbre n'est pas une feuille, pose la question
        if not estFeuille(self.arbre):
            self.changement_question(reponse)
            
        #* Si c'est une feuille
        else:
            #* Récupère le numéro d'étape
            etape = self.etape_resultat  # Suivant le numéro de l'étape, l'ordinateur saura quoi faire
            multiplicateur = 1  # Permet de définir la valeur d'ajout à etape_resultat après l'exécution d'une étape
            
            #* Étape 0, correspond à quand l'utilisateur doit dire "oui" ou "non" pour l'animal proposé
            if etape == 0:
                reponse = reponse.strip().lower()
                if reponse == "oui": # Si oui, dit qu'il a gagné, et modifie le multiplicateur pour aller à l'étape rejouer après
                    self.variable_texte.set("Super ! J'ai encore gagné !")
                    multiplicateur = 3
                    self.fenetre.update()
                    sleep(2)
                    self.variable_texte.set("Veux-tu rejouer ?")
                elif reponse == "non": #Si non, demande ce que c'était
                    self.variable_texte.set("C'était quoi alors ? :c")
                else: # Sinon, demande de répondre par oui ou non
                    self.variable_texte.set("Répond par oui ou par non s'il te plaît !")
                    self.fenetre.update()
                    sleep(2)
                    self.variable_texte.set(f"Je pense que c'est un {self.arbre} ! Ai-je raison ?")
                    
            elif etape == 1:
                self.stock_animal_attendu = reponse
                self.variable_texte.set(f"Donne une question : oui pour {self.arbre}, non pour {reponse}")
                
            elif etape == 2:
                self.variable_texte.set("Veux-tu rejouer ?")
                with open("arbre_akinator.pik", "rb") as fichierArbre: # Lit le fichier de sauvegarde
                    arbre_stocke = pickle.load(fichierArbre)
                arbre = ajoute(reponse, self.arbre, self.stock_animal_attendu, arbre_stocke)
                with open("arbre_akinator.pik", "wb") as fichierArbre: # Modifie le fichier de sauvegarde
                    pickle.dump(arbre, fichierArbre)
                self.stock_animal_attendu = "" # Remise à 0 de la variable de stockage de l'arbre attendu en cas de rejeu
                
            elif etape == 3:
                reponse = reponse.strip().lower()
                if reponse == "oui":
                    with open("arbre_akinator.pik", "rb") as fichierArbre:
                        self.arbre = pickle.load(fichierArbre)
                    self.lancement_jeu()
                else:
                    self.variable_texte.set("Merci d'avoir joué !")
                    self.fenetre.update()
                    sleep(2)
                    self.fenetre.destroy()
            self.etape_resultat += 1 * multiplicateur
    
    def changement_question(self, reponse):
        reponse = reponse.strip().lower()
        if reponse == "oui":
            self.arbre = filsGauche(self.arbre)
        elif reponse == "non":
            self.arbre = filsDroit(self.arbre)
        else:
            self.variable_texte.set("Répond par oui ou par non s'il te plaît !")
            self.fenetre.update()
            sleep(2)
        question = racine(self.arbre)
        if estFeuille(self.arbre):
            question = f"Je pense que c'est un {self.arbre} ! Ai-je raison ?"
        self.variable_texte.set(question)
        
        
partie = Akinator()