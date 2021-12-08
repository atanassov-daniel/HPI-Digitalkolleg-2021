# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# converter.py
#
# Schreibe eine Funktion converter, die einen string und beliebig viele Schlüsselwort
# Argumente entgegen nimmt. Nun ersetze alle Buchstaben, die durch ein Schlüsselwort
# neu definiert wurden, mit dem übergebenen Wert. Alle Schlüsselworte die
# berücksichtigt werden müssen, bestehen aus einem Buchstaben und einer beliebigen
# Zeichenkette als Wert.
#
# Beispiele:
#       converter("cool", o="0")
#       >>> c00l
#       converter("hacker", e="3")
#       >>> hack3r
#       converter("btw", b="by ", t="the ", w="way")
#       >>> by the way
#
# Tipp: Um zu überprüfen ob ein Buchstabe definiert ist, ohne das Python
#       einen Fehler wirft, kannst du die funktion dict.get() nutzen.
#       Nutze Google und REPL um zu sehen wie man dict.get() nutzt.
#
# Für Fortgeschrittene zusätzlich:
#       Schreibt einen Kommentar warum **kwargs gegenenfalls nicht die optimale
#       Lösung ist. Begründet eure Meinung mit Beispielen, wo diese Funktion einen
#       Buchstaben nicht verarbeiten kann.
#       Schlagt eine alternative Implementierung der Funktion vor, welche das
#       gleiche Problem löst. (Eine Änderung der Funktionssignatur ist erlaubt.)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def converter(string, **kwargs):
    kwargs_length = len(kwargs)

    if kwargs_length == 0:
        print(string)
        return

    for keyword, value in kwargs.items():
        if len(keyword) > 1:
            continue
        string = string.replace(keyword, value)

    print(string)
    """ for index in range(len(string)):
        char = string[index]
        keyword = kwargs.get(char)

        if keyword == None:
            continue
        string[index] = keyword
    
    print(string) """

converter("cool", o="0")  # >>> c00l
converter("hacker", e="3")  # >>> hack3r
converter("btw", b="by ", t="the ", w="way")  # >>> by the way