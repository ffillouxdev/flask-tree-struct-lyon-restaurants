#data_structures/recursiveTree.py

class Noeud:
    def __init__(self, info=None):
        self.info = info
        self.fg = None
        self.fd = None

class recursiveTree:
    def __init__(self, racine: Noeud):
        self.racine = racine

    def parcours_prefixe(self, noeud: Noeud):
        # prefixe : noeud, sous-arbre gauche, sous-arbre droit

        if noeud is not None:
            print(noeud.info)
            self.parcours_prefixe(noeud.fg)
            self.parcours_prefixe(noeud.fd)

    def parcours_infixe(self, noeud: Noeud):
        # infixe : sous-arbre gauche, noeud, sous-arbre droit
        if noeud is not None:
            print("suivi du parcours de noeud :", noeud.info)
            self.parcours_infixe(noeud.fg)
            print(noeud.info)
            self.parcours_infixe(noeud.fd)

    def parcours_postfixe(self, noeud: Noeud):
        # postfixe : sous-arbre gauche, sous-arbre droit, noeud

        if noeud is not None:
            self.parcours_postfixe(noeud.fg)
            self.parcours_postfixe(noeud.fd)
            print(noeud.info)
