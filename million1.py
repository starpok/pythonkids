import random
Kapital = random.randint(2,10)*10000
print("Du hast im Lotto " + str(Kapital) + " Euro gewonnen!")
print("Das solltest du nicht gleich verprassen, ")
print("Sondern lieber mit zinsen anlegen!")
print("Wie hoch soll der Zinssatz sein: ")
Prozent = float(input())
Laufzeit = 0
while Kapital < 1000000 :
  Zinsen   = Kapital * Prozent / 100
  Kapital  = Kapital + Zinsen
  Laufzeit += 1
print("Zum Millionaer brauchst du")
print(str(Laufzeit) +  "Jahr / Jahre.")