import random
Regel = "Ich denke mir eine Zahl zwischen 1 und 1000"
Zufall = random.randint(1,1000)
# print(Zufall)
print(Regel)
Versuche = 0
Eingabe = 0

# Raten

while Eingabe != Zufall :
  print("Rate mal: ")
  Eingabe = int(input())
  Versuche = Versuche + 1       
  if Eingabe < Zufall :    
     print("Zu klein!")
  if Eingabe > Zufall :
     print("Zu gross!")
  if Eingabe == Zufall :
     print("Richtig")

print("Du hast " + str(Versuche) + " Mal geraten.")
