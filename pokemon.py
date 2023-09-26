class Pokemon():
    def __init__(self, nom: str, poids: int):
        self.__nom = nom
        self.__poids = poids

    @property
    def poids(self):
        return self.__poids

    def __str__(self):
        return f"Je suis le Pokémon {self.__nom} mon poids est de {self.__poids}"
class PokemonTerre(Pokemon): 
    
    
    def __init__(self, nom:str, poids:int, nbPattes:int, taille:int):
        super().__init__(nom, poids)
        self.__nbPattes = nbPattes
        self.__taille = taille

    def vitesse(self) -> int:
        return self.__nbPattes * self.__taille * 3

    def __str__(self):
        return super().__str__() + f" ma vitesse est de {self.vitesse()} km/h et j'ai {self.__nbPattes} pattes, et je mesure {self.__taille} mètres."
        
class PokemonMaritime(Pokemon):
    def __init__(self, nom:str, poids:int, nbNageoire:int):
        super().__init__(nom, poids)
        self.__nbNageoire = nbNageoire

    def vitesse(self) -> int:
        return self.__nbNageoire * self.poids/25

    def __str__(self):
        return super().__str__() + f" ma vitesse est de {self.vitesse()} km/h et j'ai {self.__nbNageoire} nageoires"


class PokemonSportif(PokemonTerre):
    def __init__(self, nom, poids, nbPattes, taille, freqcardiaque):
        super().__init__(nom, poids, nbPattes, taille)
        self.__freqcardiaque = freqcardiaque
        
    def __str__(self):
        return super().__str__() + f"ma fréquence cardiaque est de {self.__freqcardiaque} BPM"

class PokemonCasanier(PokemonTerre):
    def __init__(self, nom, poids, nbPattes, taille, heuretv):
        super().__init__(nom, poids, nbPattes, taille)
        self.__heuretv = heuretv

    def __str__(self):
        return super.__str__() + f" et je regarde la télé {self.__heuretv} par jour"

class PokemonMer(PokemonMaritime):
    def __init__(self, nom, poids, nbNageoire):
        super().__init__(nom, poids, nbNageoire)

class PokemonCroisiere(PokemonMaritime):
    def __init__(self, nom, poids, nbNageoire):
        super().__init__(nom, poids, nbNageoire)

    def vitesse(self) -> float:
        return round(super().vitesse()/2,0)

Pikachu = PokemonSportif("Pikachu", 53, 4, 1, 85)
print(Pikachu)
print(vars(Pikachu))

Poissonglobe = PokemonCroisiere("Pufferfish", 15, 3)
print(Poissonglobe)
print(vars(Poissonglobe))
        
