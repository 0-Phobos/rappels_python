def plusgrand(a: int, b: int) -> int:
    """

    :param a: nombre 1
    :param b: nombre 2
    :return: réponse
    """
    return max(a, b)

def seuil(a : int, b : int = 10) -> bool:
    return a>b

def biggestNumber(a : list) -> int:
    return max(a)

def seuilListe(a : list, seuil : int = 3) -> int:
    listinf = []
    for i in a:
        if i < seuil:
            listinf.append(i)
    return (listinf)

def dicoliste (chain : str = "Affichage", **kwargs) :
    for key , values in kwargs.items() :
        print(f"{chain} -> {key} : {values}")


print(plusgrand(52, 53))
print(seuil(15, 25))
print(biggestNumber([10, 15, 65, 32, 562]))
print(seuilListe([10, 15, 65, 32, 562], 90))
print(dicoliste("jaaj",a="Real", b="Python", c="Is", d="Great", e=125))

