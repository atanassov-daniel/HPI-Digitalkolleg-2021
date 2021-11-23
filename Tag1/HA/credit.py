# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# credit.py - Fortgeschrittene
# Mit Kreditkarten kann man Produkte kaufen. Dazu muss der Zahlungsabwickler wissen,
# welche Karte und welches Konto eine bestimmte Zahlung veranlasst. Um Kreditkarten
# eindeutig zu identifizieren, sind diese mit einer eindeutigen Zahlenfolge bedruckt.
# Diese Zahlenfolge erfüllen bestimmte Eigenschaften, die es Computern ermöglichen
# falsche Eingaben des Nutzers in vielen Fällen auch ohne Abfrage der Datenbank zu
# erkennen.
# Der dazu entwickelte Algorithmus nennt sich "Luhn's Algorithm".
# Eure Aufgabe ist es, eine Kreditkartennummer vom Nutzer entgegen zu nehmen und
# zu überprüfen ob diese (syntaktisch) korrekt ist. Dafür müsst ihr Luhn's Algorithm implementieren.
#
# Luhns Algorithmus:
#       Der Luhn-Algorithmus erzeugt eine Prüfsumme.
#       Um diese Prüfsumme zu berechnen nimmt man jede zweite Ziffer von hinten
#       und multipliziert diese mit 2. Dann geht man die *Ziffern* des Produktes
#       durch und addiert jede einzelne Ziffer zur Prüfsumme.
#       Jede andere Ziffer in der Kreditkartennummer addieren wir direkt auf die Prüfsumme.
#       Eine Kreditkartennummer ist valide, wenn die letzte Ziffer der Prüfsumme 0 ist.
# Tipp: In Python können ints beliebing viele Bytes lang sein, also macht euch
#       keine Sorgen um zu große Zahlen.
#       Bedenkt das Ihr auf die i'te Zahl in einem string mit string[i] zugreifen könnt
#       und indexe bei 0 beginnen.
#
# Test-Input:
#       Die folgenden Kreditkartennummern sind valide:
#           4003600000000014
#           374245455400126
#           378282246310005
#           6250941006528599
#           60115564485789458
#           6011000991300009
#           3566000020000410
#           3530111333300000
#           5425233430109903
#           5425233430109903
#           2223000048410010
#           4263982640269299
#           6062826786276634
#           6271701225979642
#           6034883265619896
#       Die folgenden Kreditkartennummern sind invalide:
#           5
#           4843905893480
#           7298342937489273489
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Der Luhn-Algorithmus erzeugt eine Prüfsumme. Um diese Prüfsumme zu berechnen nimmt man jede zweite Ziffer von hinten
# und multipliziert diese mit 2. Dann geht man die *Ziffern* des Produktes durch und addiert jede einzelne Ziffer zur Prüfsumme.
# Jede andere Ziffer in der Kreditkartennummer addieren wir direkt auf die Prüfsumme.  Eine Kreditkartennummer ist valide,
# wenn die letzte Ziffer der Prüfsumme 0 ist.

password = input("Passowort: ")
pass_str = str(password)
sum = 0
last_digit = len(pass_str) - 1

i = last_digit
while i >= 0:
    digit = int(pass_str[i])

    if i % 2 == last_digit % 2:  # letzte ziffer und jede zweite von der letzten
        sum += digit
    else:  # jede zweite ziffer von der vorletzten
        product = digit * 2
        if product // 10 == 0:
            sum += product
        else:
            sum += product % 10
            sum += product // 10
    i -= 1

if sum % 10 == 0:
    print("Valid!")
else:
    print("Invalid!!!")

valids15 = [
    4003600000000014, 374245455400126, 378282246310005, 6250941006528599,
    60115564485789458, 6011000991300009, 3566000020000410,3530111333300000,
    5425233430109903, 5425233430109903, 2223000048410010, 4263982640269299, 
    6062826786276634, 6271701225979642, 6034883265619896,
]
