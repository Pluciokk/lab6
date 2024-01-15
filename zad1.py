import random
#a
numery = random.randint(1,100)

print(f"Szczesliwy numer to: {numery}")

#b
rocznik = [2001,2002,2003,2004,2005,2006]

rocznik = random.choice(rocznik)

print(f"Szczesliwy rocznik to: {rocznik}")
#c
print("Numerki lotto to: ", random.sample(range(1,49), 6))

