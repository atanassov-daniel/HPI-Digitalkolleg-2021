# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# cash.py
# Deine Aufgabe ist einen Geldbetrag in Cent einzulesen und die geringstmögliche
# Anzahl an Münzen mit Stückzahl auszugeben.
# Die möglichen Münzen sind: 2 EUR, 1 EUR, 50 Cent, 10 Cent, 5 Cent, 2 Cent und 1 Cent.
# Eine mögliche Ausgabe sieht so aus:
#
#        Wir brauchen 0 mal 200 Cent.
#        Wir brauchen 0 mal 100 Cent.
#        Wir brauchen 1 mal 50 Cent.
#        Wir brauchen 1 mal 20 Cent.
#        Wir brauchen 0 mal 10 Cent.
#        Wir brauchen 1 mal 5 Cent.
#        Wir brauchen 0 mal 2 Cent.
#        Wir brauchen 1 mal 1 Cent.
#
# Noch zwei Tipps:  Stelle die Geldbeträge als ganze Cent zahlen da.
#                   Mit dem // Operator kann man abgerundete ganzzahlige Divison betreiben.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

amount = int(input("Betrag in Cent: "))

current = amount

cent200=current//200
print(f'Wir brauchen {cent200} mal 200 Cent.')
current=current-200*cent200

cent100=current//100
print(f'Wir brauchen {cent100} mal 100 Cent.')
current=current-100*cent100

cent50=current//50
print(f'Wir brauchen {cent50} mal 50 Cent.')
current=current-50*cent50

cent20=current//20
print(f'Wir brauchen {cent20} mal 20 Cent.')
current=current-20*cent20

cent10=current//10
print(f'Wir brauchen {cent10} mal 10 Cent.')
current=current-10*cent10

cent5=current//5
print(f'Wir brauchen {cent5} mal 5 Cent.')
current=current-5*cent5

cent2=current//2
print(f'Wir brauchen {cent2} mal 2 Cent.')
current=current-2*cent2

cent1=current//1
print(f'Wir brauchen {cent1} mal 1 Cent.')
current=current-1*cent1

""" obj = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
while current > 0:
    if(current % 200 == 0): obj[200]=obj[200]+1; current-=200; print(current); print(obj[200]); break; """

