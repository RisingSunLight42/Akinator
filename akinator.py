from fonctions_primaires import estFeuille, racine


import fonctions_primaires as func_prim

monArbre = ["vit-il dans la maison ?", # Racine de départ
            ["a-t-il des poils ?", ["miaule-t-il ?", "Chat", "Hamster"], "Poisson rouge"],  # Arbre Gauche
            ["est-il dangereux ?", ["vole-t-il ?", "Frelon", "Tigre"], "Herisson"]]  # Arbre Droit

def jeu1(arbre):
    print("Pense à un animal.")
    while not func_prim.estFeuille(arbre):
        reponse = input(func_prim.racine(arbre))