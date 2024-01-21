import random
from functools import reduce
def srednia(a):
    liczba = reduce(lambda x,y: x*y,a)
    return liczba**(1.0/len(a))
x = int(input("Podaj dolny zakres: "))
y = int(input("Podaj górny zakres: "))
krotka = tuple(random.randint(x,y) for i in range(10))
sredniaa = srednia(krotka)
print("Srednia geometryczna krotki to",sredniaa)
