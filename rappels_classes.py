class Tasse :
    matiere : str = "Céramique"
    def __init__(self, couleur : str, contenance : int, marque : str):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

    def  content (self, boisson : str):
        self.contenu = boisson

    def boissonbue(self):
        del self.contenu

    def __str__(self):
        if hasattr(self, 'contenu'):
            return f"La tasse de matière {self.matiere} de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml remplie de {self.contenu}"
        else :
            return f"La tasse de matière {self.matiere} de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml est vide"


mT = Tasse("bleue", 50, "Pyrex")
mT.content("Coca")
print(mT)
mT.boissonbue()
print(mT)

