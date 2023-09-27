import pickle

class Personnage():
    """
    Cette classe permet de définir un personnage avec un pseudonyme, un niveau par default a 1, et des pdv et un niveau d'initiative initialement de meme valeur que le niveau

    .. py:attribute:: pseudo:
        pseudo du personnage
        :type: str

    .. py:attribute:: niveau:
        niveau, point de vie et initiative du personnage
        :type: int
    """
    def __init__(self, pseudo:str,niveau:int=1):
        self.__pseudo=pseudo
        self.__niveau=niveau
        self.__point_de_vie=niveau
        self.__initiative=niveau

    def __str__(self):
        return f"Ce personnage de niveau {self.__niveau} s'appelle {self.__pseudo} a {self.__initiative} d'initiative et {self.__point_de_vie}pv"

    @property
    def pseudo(self):
        return self.__pseudo

    @property
    def niveau(self):
        return self.__niveau

    @property
    def point_de_vie(self):
        return self.__point_de_vie

    @point_de_vie.setter
    def point_de_vie(self,nouveau_point_de_vie):
        self.__point_de_vie=nouveau_point_de_vie

    @property
    def initiative(self):
        return self.__initiative

    @initiative.setter
    def initiative(self,value):
        self.__initiative=value

    @classmethod
    def load(cls,path:str):
        """
        Charge un personnage depuis un fichier binaire
        :param path: le chemin du fichier binaire
        :return:
        """
        with open(path,'rb') as f:
            return pickle.load(f)

    def save(self,path:str):
        """
            sauvegarde un personnage vers un fichier binaire
            :param path: le chemin du fichier binaire
            :return:
        """
        with open(path, 'wb') as f:
            pickle.dump(self,f)

    def degat(self):
        return self.niveau

    def attack(self,cible:'Personnage'):
        """
            fonction permettant d'attaquer un autre personnage

            :param cible: le personnage adversaire
            :type cible: Personnage
            :return: none
            :rtype: void
        """
        if self.__initiative>cible.initiative:
            cible.point_de_vie=cible.point_de_vie-self.degat()
            if cible.point_de_vie>0:
                self.__point_de_vie-=cible.degat()

        elif self.__initiative<cible.initiative:
            self.__point_de_vie -= cible.degat()
            if self.__point_de_vie>0:
                cible.point_de_vie=cible.point_de_vie - self.degat()

        elif self.__initiative==cible.initiative:
            self.__point_de_vie -= cible.degat()
            cible.point_de_vie=cible.point_de_vie - self.degat()

    def combat(self,cible:'Personnage'):
        """
            fonction permettant de combattre a la mort un autre personnage

            :param cible: le personnage adversaire
            :type cible: Personnage
            :return: none
            :rtype: void
        """
        while self.point_de_vie>0 and cible.point_de_vie>0:
            self.attack(cible)
            print(f"Attaquant : {self.point_de_vie}pv\nDefenseur : {cible.point_de_vie}pv\n")

        if self.point_de_vie<0:
            self.point_de_vie=0
        if cible.point_de_vie<0:
            cible.point_de_vie=0

    def heal(self):
        """
            fonction permettant de regenerer tous ses points de vie
            :return: none
            :rtype: void
        """
        self.point_de_vie=self.niveau

class Guerrier(Personnage):
    """
        Cette classe permet de définir un guerrier qui herite d'un personnage, avec un pseudonyme, un niveau par default a 1,

        .. py:attribute:: pseudo:
            pseudo du guerrier
            :type: str

        .. py:attribute:: niveau:
            niveau du guerrier
            :type: int
        """
    def __init__(self, pseudo:str,niveau:int=1):
        super().__init__(pseudo, niveau)
        self.point_de_vie = niveau*8+4
        self.initiative = niveau*4+6


    def degat(self):
        return self.niveau*2

    def heal(self):
        """
            fonction permettant de regenerer tous ses points de vie
            :return: none
            :rtype: void
        """
        self.point_de_vie = self.niveau * 8 + 4

class Mage(Personnage):
    """
            Cette classe permet de définir un mage qui herite d'un personnage, avec un pseudonyme, un niveau par default a 1,

            .. py:attribute:: pseudo:
                pseudo du mage
                :type: str

            .. py:attribute:: niveau:
                niveau du mage
                :type: int
    """
    def __init__(self, pseudo:str,niveau:int=1):
        super().__init__(pseudo, niveau)
        self.point_de_vie = niveau*5+10
        self.initiative = niveau*6+4
        self.__mana=niveau*5

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, new_mana):
        self.__mana=new_mana

    def degat(self):
        if self.mana>0:
            self.mana-=4
            return self.niveau+3
        return self.niveau

    def heal(self):
        """
            fonction permettant de regenerer tous ses points de vie
            :return: none
            :rtype: void
        """
        self.point_de_vie = self.niveau * 5 + 10

class Joueur:
    """
    Cette classe permet de définir un joueur. Un joueur possède un nom, et un ensemble de personnages stocké dans une liste

    .. py:attribute:: nom:
        pseudo du joueur
        :type: str

    .. py:attribute:: max_personnages:
        nombre maximum de personnages du joueur.
        :type: int
    """
    def __init__(self, nom:str, max_personnages:int):
        self.__nom=nom
        self.__max_personnages=max_personnages
        self.__list_personnages=[]

    def __str__(self):
        return f"le joueur {self.__nom} a une capacite maximum de {self.__max_personnages} et contient pour l'instant {len(self.__list_personnages)} personnages"

    @property
    def list_personnages(self):
        return self.__list_personnages

    def add_personnage(self,Personnage:Personnage):
        """
            fonction d'ajouter un personnage a la liste des personnages du joueur
            :return: none
            :rtype: void
        """
        if len(self.__list_personnages) < self.__max_personnages:
            self.__list_personnages.append(Personnage)

    def select_personnage(self, arg):
        """
            fonction qui permet de selectionner un personnage de la liste des personnages du joueur
            :return: Personnage
            :rtype: Personnage
        """
        if type(arg)==int:
            return self.__list_personnages[arg]
        if type(arg)==str:
            for el in self.__list_personnages:
                if el.pseudo==arg:
                    return el
        elif arg in self.__list_personnages:
            return arg


    def remove_personnage(self, arg):
        """
            fonction qui permet de supprimer un personnage de la liste des personnages du joueur
            :return: none
            :rtype: void
        """
        if type(arg)==int:
            self.__list_personnages.pop(arg)
        elif type(arg)==str:
            for el in self.__list_personnages:
                if el.pseudo==arg:
                    self.__list_personnages.remove(el)
        else : self.__list_personnages.remove(arg)
