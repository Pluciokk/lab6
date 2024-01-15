from datetime import datetime

laborki = datetime(2023,12,19)
kolos = datetime(2024,2,12)

roznicalab = datetime.now() - laborki
roznicakolo = kolos - datetime.now()

print(f"Od ostatnich laborek mineło: {roznicalab}")
print(f"Do kolosa zostalo: {roznicakolo}")