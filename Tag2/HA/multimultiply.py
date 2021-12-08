# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# multimultiply.py
#
# Schreibe eine Funktion multimultiply welche eine beliebige Anzahl von ganzen Zahlen
# einliest und diese dann multipliziert. Gib das Ergebnis zurück.
# Beschreibe in einem Docstring wie sich deine Funktion verhält. Gehe vor allem
# auf den Fall ein, wenn keine Eingabe übergeben wird.
#
# Tipp: Wenn du deinen Docstring geschrieben hast, dann füge mal diese Zeile an
#       an das Ende deines Programmes:
#           print(help(multimultiply))
#       Du kannst die interaktive Sitzung mit q beenden.
#       Mehr Details findest du in der offiziellen Dokumentation von Python:
#           https://docs.python.org/3/library/functions.html#help
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def multimultiply(*args):
    r"""Die Funktion liest eine beliebige Anzahl von ganzen Zahlen ein und multipliziert dann diese.
    Am Ende gibt die Funktion das Ergebnis zurück.
    In dem Fall, wenn keine Eingabe übergeben wird, gibt die Funktion "No numbers"(should it be 0?) zurück.
    """
    if len(args) == 0:
        return "Keine Zahlen wurden eingegeben"
    if len(args) == 1:
        return args[0]

    multi = 1
    for num in args:
        multi *= num
    return multi
    


# Test your function
print(multimultiply(11, 36))
print(multimultiply(18, 6, 1, 16, 27, 35))
print(multimultiply())
print(multimultiply(20, 32, 30, 26, 33, 8))
print(multimultiply(1, 5, 0, 8, 1))

print(help(multimultiply))