monArbre = ["vit-il dans la maison ?", # Racine de départ
            ["a-t-il des poils ?", ["miaule-t-il ?", "Chat", "Hamster"], "Poisson rouge"],  # Arbre Gauche
            ["est-il dangereux ?", ["vole-t-il ?", "Frelon", "Tigre"], "Herisson"]]  # Arbre Droit


def creerArbre(racine, gauche, droit):
    """Permet de créer un arbre, avec une racine et deux fils"""
    return [racine, gauche, droit]


def estFeuille(arbre):
    """Renvoie si l'arbre donné est une feuille"""
    return type(arbre) == str


def racine(arbre):
    """Renvoie la racine de l'arbre"""
    return arbre[0]


def filsGauche(arbre):
    """Renvoie le fils gauche de l'arbre"""
    return arbre[1]


def filsDroit(arbre):
    """Renvoie le fils droit de l'arbre"""
    return arbre[2]


def nbNoeud(arbre):
    """Renvoie le nombre de noeuds"""
    if estFeuille(arbre):
        return 1
    return 1 + nbNoeud(filsGauche(arbre)) + nbNoeud(filsDroit(arbre))
    
    
def nbFeuille(arbre):
    """Renvoie le nombre de feuilles"""
    if estFeuille(arbre):
        return 1
    return nbFeuille(filsGauche(arbre)) + nbFeuille(filsDroit(arbre))


def animalPresent(animal, arbre):
    """Renvoie si un animal est présent ou pas"""
    if estFeuille(arbre):
        return arbre == animal
    return animalPresent(animal, filsGauche(arbre)) or animalPresent(animal, filsDroit(arbre))


def questionPresente(question, arbre):
    """Renvoie si une question est présente dans l'arbre ou pas"""
    if estFeuille(arbre):
        return False
    if racine(arbre) == question:
        return True
    return questionPresente(question, filsGauche(arbre)) or questionPresente(question, filsDroit(arbre))
    
    
def listeAnimal(arbre):
    """Renvoie une liste des animaux de l'arbre"""
    if estFeuille(arbre):
        return [arbre]
    arbre_gauche = listeAnimal(filsGauche(arbre))  # Récupère la valeur de listeAnimal de l'arbre gauche
    arbre_droit = listeAnimal(filsDroit(arbre))    # Récupère la valeur de listeAnimal de l'arbre droit
    liste = [element for element in arbre_gauche]  # Initialisation d'une variable liste qui se construit sur arbre_gauche
    liste += [element for element in arbre_droit]  # Lui ajoute les éléments d'arbre droit
    return liste                                   # Renvoie la liste


def lesquels(question, arbre):
    """Renvoie une liste des animaux vérifiant la caractéristique"""
    if racine(arbre) == question:  # Vérifie si la racine de l'arbre est la question recherché
        return listeAnimal(filsGauche(arbre))  # Si oui, utilise la fonction listeAnimal pour lister les animaux liés à la question, uniquement le filsGauche car on veut le oui
    if estFeuille(arbre):  # Si jamais l'arbre est une feuille, renvoie une liste vide car il n'a pas répondu au précédent test d'arrêt
        return []
    else:
        return lesquels(question, filsGauche(arbre)) + lesquels(question, filsDroit(arbre)) # Si pas de résultats appelle la fonction sur le fils gauche et droit de l'arbre


def ajoute(question, animal1, animal2, arbre):
    """Ajoute une question donnée dans l'arbre, dont la réponse est oui pour animal1 et non pour animal2.
    Si animal1 n'est pas dans arbre, on renvoie l'arbre d'origine.

    Args:
        question (str): Question à ajouter.
        animal1 (str): Premier animal, il doit être obligatoirement présent dans l'arbre.
        animal2 (str): Second animal, il ne doit pas être dans l'arbre.
        arbre (list): Arbre auquel on veut ajouter la question.
    """
    if not animalPresent(animal1, arbre):  # Si animal1 n'est pas présent dans l'arbre, on renvoie l'arbre initial
        return arbre
    if estFeuille(arbre):                        # Si l'arbre est une feuille
        if arbre == animal1:                     # Si cette feuille est l'animal que l'on souhaite remplacer par une question
            return [question, animal1, animal2]  # Renvoi le nouvel arbre, avec la question, l'animal1 en oui et l'animal 2 en non
        return arbre                             # Sinon renvoi juste la feuille
    else:  # Si c'est pas une feuille
        arbre_gauche = ajoute(question, animal1, animal2, filsGauche(arbre))  # Récupère l'ajout de l'arbre_gauche
        arbre_droit = ajoute(question, animal1, animal2, filsDroit(arbre))    # Récupère l'ajout de l'arbre_droit
        return [racine(arbre), arbre_gauche, arbre_droit]                     # Renvoie une liste contenant la racine puis l'arbre gauche et l'arbre droit
