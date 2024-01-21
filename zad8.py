import math

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj kąt: "))

if a <= 0 or b <= 0 or c <= 0 or c>=90:
    print("Nie istnieje taki trójkąt")
else:
    stopnie = math.radians(c)

    if a**2 + b**2 <= (a + b)**2 * math.sin(stopnie)**2:
        print("Trójkąt nie jest ostrokątny")
    else:
        p = 0.5* a * b * math.sin(stopnie)
        print("Pole trojkąta wynosi",p)
