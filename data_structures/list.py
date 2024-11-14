# data structure/pileTree.py
class MaListe:
    def __init__(self):
        self.liste = []

    def ajouter(self, element):
        self.liste.append(element)

    def supprimer(self, val):
        if val in self.liste:
            self.liste.remove(val)
        else:
            print("La valeur n'existe pas dans la liste")

    def afficher(self):
        if len(self.liste) == 0:
            print("La liste est vide")
        return self.liste

    def obtenir(self, index):
        if index < len(self.liste):
            return self.liste[index]
        else:
            return -1

    def trouver_indice(self, element):
        if element in self.liste:
            return self.liste.index(element)
        else:
            return -1

    def taille(self):
        return len(self.liste)

    def inverser(self):
        self.liste.reverse()
        return self.liste

    def vider(self):
        return self.liste.clear()

    def contient(self, element):
        if isinstance(element, dict):
            for i in self.liste:
                if i == element:
                    return True
            return False
        else:
            for i in self.liste:
                if element in i:
                    return True
            return False

    """
    Pour une liste et un dictionnaire, compter le nombre d'occurrence
    """

    def compter(self, element):
        if isinstance(element, dict):
            count = 0
            for i in self.liste:
                if i == element:
                    count += 1
            return count
        else:
            count = 0
            for i in self.liste:
                if element in i:
                    count += 1
            return count

    def trier(self):
        if isinstance(self.liste[0], dict):
            return self.liste.sort(key=lambda x: x["key"])
        else:
            return self.liste.sort()
        
    def trouver_doublons(self):
        if isinstance(self.liste[0], dict):
            doublon_dic = {}
            for i in self.liste:
                if self.compter(i) > 1:
                    doublon_dic[tuple(i.items())] = self.compter(i)
            return doublon_dic
        
        else:
            doublon_list = []
            for i in self.liste:
                if self.compter(i) > 1:
                    doublon_list.append(i)
            return doublon_list
            
    
    def filtrer_uniques(self):
        if isinstance(self.liste[0], dict):
            unique_dic = {}
            for i in self.liste:
                if self.compter(i) == 1:
                    unique_dic[tuple(i.items())] = 1
            return unique_dic
        else:
            unique_list = []
            for i in self.liste:
                if self.compter(i) == 1:
                    unique_list.append(i)
            return unique_list
    
    def k_plus_grand():
        pass
        


if __name__ == "__main__":
    # une liste (exo1)
    """
    liste = MaListe()
    for i in range(10):
        liste.ajouter(random.randint(0, 100))
    print(liste.afficher())

    print("suppression\n")
    liste.supprimer(10)
    print(liste.afficher())

    print("obtenir\n")
    print(liste.obtenir(4))

    print("trouver indice\n")
    print(liste.trouver_indice(4))

    print("taille\n")
    print(liste.taille())

    print("inverser\n")
    print(liste.inverser())
    """

    # un dictionnaire (exo2)
    """
    dic = MaListe()
    dic.ajouter({"key": "value", "age": 20, "nom": "toto"})
    print(dic.contient({"key": "value"}))
    print(dic.contient("key"))
    print(dic.afficher())

    print("vider\n")
    print(dic.vider())
    print(dic.afficher())

    print("compter\n")
    dic.ajouter({"key": "value2", "age": 25, "nom": "titi"})
    dic.ajouter({"key": "value1", "age": 20, "nom": "toto"})
    print(dic.afficher())
    print(dic.compter({"key": "value", "age": 20, "nom": "toto"}))

    print("trier\n")
    print(dic.trier())
    print(dic.afficher())
    """
    
    # (exo 3)
    dic2 = MaListe()
    dic2.ajouter({"key": "value1", "age": 22, "nom": "toto"})
    dic2.ajouter({"key": "value1", "age": 22, "nom": "toto"})
    dic2.ajouter({"key": "value3", "age": 21, "nom": "titi"})
    dic2.ajouter({"key": "value2", "age": 25, "nom": "tata"})
    dic2.ajouter({"key": "value2", "age": 26, "nom": "tutu"})
    print(dic2.afficher())
    print(dic2.trouver_doublons())
    print(dic2.filtrer_uniques())