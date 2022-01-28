from fonctions_primaires import estFeuille, racine


import fonctions_primaires as func_prim

monArbre = ["vit-il dans la maison ?", # Racine de départ
            ["a-t-il des poils ?", ["miaule-t-il ?", "Chat", "Hamster"], "Poisson rouge"],  # Arbre Gauche
            ["est-il dangereux ?", ["vole-t-il ?", "Frelon", "Tigre"], "Herisson"]]  # Arbre Droit

def jeu1(arbre):
    """Fonction simulant le déroulé d'un Akinator

    Args:
        arbre (list): Arbre binaire contenant les questions qu'Akinator posera, ainsi que les réponses finales.
    """
    print("Pense à un animal.")                         # Demande au joueur de penser à l'animal qu'il souhaite faire deviner
    while not func_prim.estFeuille(arbre):              # Tant que l'arbre n'est pas une feuille (donc un animal)
        reponse = input(f"{func_prim.racine(arbre)} ")  # Il pose au joueur la question
        if reponse.lower().strip() == "oui":            # Si elle est oui, l'arbre devient le filsGauche de l'arbre
            arbre = func_prim.filsGauche(arbre)
        elif reponse.lower().strip() == "non":          # Si elle est non, l'arbre devient le filsDroit de l'arbre
            arbre = func_prim.filsDroit(arbre)
        else:                                           # Si la réponse est incorrecte, il donne un message d'erreur et repose la question
            print("La réponse entrée est invalide, répond bien par 'oui' ou 'non' !")
    print(f"C'est un {arbre} !")                        # Donne la réponse qu'il a trouvé


def jeu2(arbre):
    """Fonction simulant le déroulé d'un Akinator, mais avec en plus un système d'apprentissage

    Args:
        arbre (list): Arbre binaire contenant les questions qu'Akinator posera, ainsi que les réponses finales.
    """
    print("Pense à un animal.")                         # Demande au joueur de penser à l'animal qu'il souhaite faire deviner
    while not func_prim.estFeuille(arbre):              # Tant que l'arbre n'est pas une feuille (donc un animal)
        reponse = input(f"{func_prim.racine(arbre)} ")  # Il pose au joueur la question
        if reponse.lower().strip() == "oui":            # Si elle est oui, l'arbre devient le filsGauche de l'arbre
            arbre = func_prim.filsGauche(arbre)
        elif reponse.lower().strip() == "non":          # Si elle est non, l'arbre devient le filsDroit de l'arbre
            arbre = func_prim.filsDroit(arbre)
        else:                                           # Si la réponse est incorrecte, il donne un message d'erreur et repose la question
            print("La réponse entrée est invalide, répond bien par 'oui' ou 'non' !")
    print(f"C'est un {arbre} !")                        # Donne la réponse qu'il a trouvé
