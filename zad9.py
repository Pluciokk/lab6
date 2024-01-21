import random
a = int(input("Podaj dolny zarkes: "))
b = int(input("Podaj górny zakres: "))

losowanie = random.randint(a,b)

proby = 3

while proby > 0:
    zgadnij = int(input("Podaj liczbe:"))
    if zgadnij == losowanie:
        print("Zgadłeś liczbę!")
        break
    elif zgadnij < losowanie:
        print("Za mało.")
    else:
        print("Za dużo.")
    proby -= 1
    print("Pozostało",proby,"prób!")
if proby == 0:
    print("Koniec gry! Zabrakło ci prób!")
