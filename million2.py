print("Wie viel Geld willst du anlegen: ")
Kapital = float(input())
print("Wie hoch soll der Zinssatz sein: ")
print("Und wie lange willst du warten:")
Laufzeit = input()
Prozent = float(input())
Laufzeit = 0
while Kapital < 1000000 :
  Zinsen   = Kapital * Prozent / 100
  Kapital  = Kapital + Zinsen 
  Laufzeit += 1
if Laufzeit > 0 :
  print("Um Millionaer zu werden, musst du das Geld ")
  print(str(Laufzeit) + "Jahre auf der Bank braten lassen.")
else :
  print("Willkommen im Club der Millionaere!")  