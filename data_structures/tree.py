# data_structures/tree.py
class Noeud_:
    def __init__(self, info):
        self.info = info
        self.fg = None
        self.fd = None
        self.enfants = []

    def ajouter_enfant(self, noeud):
        self.enfants.append(noeud)


class Arbre:
    def __init__(self):
        self.racine = Noeud_("Lyon")

    def ajouter_arrondissement(self, arrondissement_nom):
        arrondissement_ = Noeud_(arrondissement_nom)
        self.racine.ajouter_enfant(arrondissement_)
        return arrondissement_

    def ajouter_type_resto(self, arrondissement, type_rest):
        type_ = Noeud_(type_rest)
        arrondissement.ajouter_enfant(type_)
        return type_

    def afficher_arbre(self, noeud=None):
        if noeud is None:
            noeud = self.racine
        print(noeud.info)
        for enfant in noeud.enfants:
            self.afficher_arbre(enfant)
            print ("--->", enfant.info)

    def contain(self, restaurant):
        if restaurant in self.racine.enfants:
            return True
        return False
    

    def recherche(self, val):
        # if self.racine == val:
        #     return self.racine
        # elif val < self.val:
        pass
