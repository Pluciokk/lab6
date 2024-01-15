import time
odlicz = int(input("Podaj czas: "))
while odlicz > 0:
    print("Do konca czasu zostało:",odlicz,"sekund")
    time.sleep(1)
    odlicz -= 1
print("Odliczanie zakonczone")

