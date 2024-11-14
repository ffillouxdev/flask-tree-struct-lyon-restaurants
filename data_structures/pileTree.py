#data_structures/pileTree.py
class Noeud:
    def __init__(self, info=None):
        self.info = info
        self.fg = None
        self.fd = None


class Pile:
    def __init__(self):
        self.pile = []

    def empiler(self, element):
        self.pile.append(element)

    def depiler(self):
        return self.pile.pop()

    def pileVide(self):
        return len(self.pile) == 0

    def sommet(self):
        return self.pile[-1]


class PileTree:
    def __init__(self, racine: Noeud):
        self.racine = racine
        self.pile = Pile()
        self.pile.empiler(racine)
        self.pile = Pile()

    def empilerNoeud(self, noeud: Noeud):
        self.pile.append(noeud)

    def afficherPile(self):
        for i in self.pile:
            print(i.info)

    def depilerNoeud(self):
        return self.pile.pop()

    def pileVide(self):
        return len(self.pile) == 0

    def parcours_prefixe(self):
        pile = self.pile
        while not pile.pileVide():
            noeud = pile.depiler()
            print(noeud.info)
            if noeud.fd is not None:
                pile.empiler(noeud.fd)
            if noeud.fg is not None:
                pile.empiler(noeud.fg)

    def infixe(self):
        pass

    def postfixe(self):
        pass
        pass

    def postfixe(self):
        pass
