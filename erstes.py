Text = "Hallo, wer da?"
print(Text)
Name = input() 
Text = "Du bist also " + Name
print(Text)
print("Und wie geht es dir?")
Antwort = input()
print("Dir geht es also " + Antwort)
if Antwort == "gut" :
    print("Das freut mich!")
if Antwort == "schlecht" :
    print("Das tut mir leid!")