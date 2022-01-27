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
    if estFeuille(arbre):
        return []
    else:
        pass