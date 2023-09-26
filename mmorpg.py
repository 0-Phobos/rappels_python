"""
Classe personnage:
Atrtibut:
    -pseudo
    -niveau
    -nombre de PV
    -initiative

Méthodes
"""




class Personnage:

    def __init__(self, pseudo:str, niveau:int=1): #on passe deux arguments pour faire deux constructeurs suivant le cas
        self.__pseudo=pseudo
        self.__niveau=niveau
        self.__nombrePV=niveau
        self.__initiative=niveau

    def get_pseudo(self):
        return self.__pseudo
    #@property
    def get_pv(self):
        return self.__nombrePV
    #@set_pv.setter
    def set_pv(self,nouveaux_PV):
        self.__nombrePV=nouveaux_PV

    def get_ini(self):
        return self.__initiative
    def set_ini(self, nouveau_ini):
        self.__initiative = nouveau_ini

    def set_niveau(self, nouveau_niveau):
        self.__niveau = nouveau_niveau
    #@get_niveau.getter
    def get_niveau(self):
        return self.__niveau

    def attaque(self, cible:'Personnage') -> None:

        if cible.get_ini() > self.__initiative:
            print("1")
            self.set_pv(self.__nombrePV - cible.degats())
            if self.__nombrePV > 0:
                cible.set_pv(cible.get_pv() - self.degats())


        elif cible.get_ini() < self.__initiative :
            print("2")
            cible.set_pv(cible.get_pv() - self.degats())
            if cible.get_pv() > 0:
                self.__nombrePV -= cible.degats()

        elif cible.get_ini() == self.__initiative :
            print("3")
            print(f"{cible.get_ini()} & {self.get_ini()} ")
            self.set_pv(self.__nombrePV - cible.degats())
            cible.set_pv(cible.get_pv() - self.degats())
        print(f"{self.get_pv()}&{cible.get_pv()}")
    def combat(self, cible:'Personnage') -> None    :
        while cible.get_pv() > 0 and self.__nombrePV > 0 :

            self.attaque(cible)
            print(f"{self.__pseudo} a maintenant {self.__nombrePV} PV, La cible a maintenant {cible.get_pv()} PV")

    def healing(self):
        self.__nombrePV += self.__niveau - self.__nombrePV

    def degats(self):
        return self.__niveau

class Guerrier(Personnage):
    def __init__(self, pseudo,niveau): #on passe deux arguments pour faire deux constructeurs suivant le cas
        super().__init__(pseudo,niveau) #Ici on spécifie que ces valeurs là sont à garder tel quel dans la classe personnage
        self.set_pv(niveau * 8 + 4)  #ici on modifie certains attributs de la classe héritée Personnage donc on les redéclares en quelques sortes
        self.set_ini(niveau * 4 +6)
        print(f"L'initiative du guerrier est : {self.get_ini()}")
        print(f'Nombre de PV du Guerrier au départ {self.get_pv()}')
        print(f'Dégats de base du Guerrier au départ {self.get_niveau() * 2}')

    def degats(self):

        return self.get_niveau() * 2


class Mage(Personnage):
    def __init__(self, pseudo, niveau):  # on passe deux arguments pour faire deux constructeurs suivant le cas
        super().__init__(pseudo, niveau)  # Ici on spécifie que ces valeurs là sont à garder tel quel dans la classe personnage
        self.set_pv(niveau * 5 + 10)# ici on modifie certains attributs de la classe héritée Personnage, il faut absoluement utiliser les getter et les setters car sinon cela crée un duplicata et le code ne saura pas lequel utiliser
        self.set_ini(niveau * 6 + 4)
        print(f"L'initiative du mage est : {self.get_ini()}")
        print(f'Nombre de PV du Mage au départ {self.get_pv()}')
        print(f'Dégats de base du Mage au départ {self.get_niveau() + 3}')
        self.__mana = niveau * 5

    def degats(self):
        if self.__mana > 0:
            self.__mana -= 4

            return self.get_niveau() + 3
        return self.get_niveau()


class Joueur:
    def __init__(self, nom: str, nbmax: int):
        self.__nom = nom
        self.__nombremax = nbmax
        self.__inventaire = []

    def ajout(self, perso: 'Personnage'):
        if len(self.__inventaire) < self.__nombremax:
            self.__inventaire.append(perso)
            print(f"{perso.get_pseudo()} a bien été ajouté à l'inventaire de {self.__nom}")


jaajman = Mage('jaaj', 5)
jeejman = Guerrier('jeej', 5)
joueurtest = Joueur('jouj', 2)

print(vars(jaajman))
print(vars(jeejman))
joueurtest.ajout(jeejman)
print(vars(joueurtest))
#jaajman.combat(jeejman)

















