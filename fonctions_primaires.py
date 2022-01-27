monArbre = ["vit-il dans la maison ?", # Racine de départ
            ["a-t-il des poils ?", ["miaule-t-il ?", "Chat", "Hamster"], "Poisson rouge"],  # Arbre Gauche
            ["est-il dangereux ?", ["vole-t-il ?", "Frelon", "Tigre"], "Herisson"]]  # Arbre Droit


def creerArbre(racine, gauche, droit):
    """Permet de créer un arbre, avec une racine et deux fils

    Args:
        racine (str): Racine de l'arbre, ici une question pour l'Akinator
        gauche (str/list): Fils gauche de l'arbre, peut-être une str, mais aussi un autre arbre (donc une liste)
        droit (str/list): Fils droit de l'arbre, peut-être une str, mais aussi un autre arbre (donc une liste)

    Returns:
        list: Arbre renvoyé, avec sa racine et ses deux fils
    """
    return [racine, gauche, droit]  # Renvoi une liste contenant la racine, puis le fils gauche et enfin le fils droit


def estFeuille(arbre):
    """Renvoie si l'arbre donné est une feuille

    Args:
        arbre (str/list): Arbre à tester

    Returns:
        boolean: Valeur booléenne si l'arbre est une feuille ou non
    """
    return type(arbre) == str  # Teste si le type de l'arbre est str et renvoi le résultat du test


def racine(arbre):
    """Renvoie la racine de l'arbre

    Args:
        arbre (list): Arbre dont l'on souhaite la racine

    Returns:
        str: Racine de l'arbre
    """
    return arbre[0]  # Renvoie la racine de l'arbre, qui est toujours en première position


def filsGauche(arbre):
    """Renvoie le fils gauche de l'arbre

    Args:
        arbre (list): Arbre dont l'on souhaite le fils gauche

    Returns:
        str: Fils gauche de l'arbre
    """
    return arbre[1]  # Renvoie le fils gauche de l'arbre, qui est toujours en seconde position


def filsDroit(arbre):
    """Renvoie le fils droit de l'arbre

    Args:
        arbre (list): Arbre dont l'on souhaite le fils droit

    Returns:
        str: Fils droit de l'arbre
    """
    return arbre[2]  # Renvoie le fils droit de l'arbre, qui est toujours en troisième position


def nbNoeud(arbre):
    """Renvoie le nombre de noeuds

    Args:
        arbre (str/list): Arbre dont l'on souhaite connaître le nombre de noeuds

    Returns:
        int: Nombre de noeuds de l'arbre donné 
    """
    if estFeuille(arbre):  # Si l'arbre est une feuille, alors renvoie 1 (car la feuille est un noeud)
        return 1
    return 1 + nbNoeud(filsGauche(arbre)) + nbNoeud(filsDroit(arbre))  # Sinon, renvoie 1 (la racine) + le nombre des noeuds des fils gauche et droit, eux-mêmes des arbres
    
    
def nbFeuille(arbre):
    """Renvoie le nombre de feuilles

    Args:
        arbre (str/list): Arbre dont l'on souhaite connaître le nombre de feuilles

    Returns:
        int: Nombre de feuilles de l'arbre donné
    """
    if estFeuille(arbre):  # Si l'arbre est une feuille, renvoie 1, car il y a une feuille de plus dans l'arbre
        return 1
    return nbFeuille(filsGauche(arbre)) + nbFeuille(filsDroit(arbre))  # Sinon, regarde si les arbres gauche et droit de l'arbre précédemment donné sont des feuilles


def animalPresent(animal, arbre):
    """Renvoie si un animal est présent ou pas dans l'arbre

    Args:
        animal (str): Animal dont l'on souhaite connaître la présence
        arbre (str/list): Arbre dans lequel on souhaite savoir si l'animal est présent

    Returns:
        boolean: Résultat True/False de la présence de l'animal donné dans l'arbre fournit
    """
    if estFeuille(arbre):       # Si l'arbre est une feuille, alors c'est un animal
        return arbre == animal  # On vérifie si cet animal est celui demandé et on renvoie le résultat
    return animalPresent(animal, filsGauche(arbre)) or animalPresent(animal, filsDroit(arbre))  # Sinon, appelle la fonction sur les arbres gauche et droit avec un OU logique


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
