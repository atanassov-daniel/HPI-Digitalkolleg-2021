# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# phonebook.py
#
# Du hast zwei verschiedenen Telefonbücher von deinem Chef erhalten.
# Damit die Verkaufsabteilung alle potentiellen Kunden genau einmal anruft, ist
# es deine Aufgabe eine einheitliche Tabelle mit allen Telenfonnummern und Kunden-
# namen zu erstellen. Achtung: Namen können mehrfach vorkommen, bezeichnen aber
# unterschiedliche Personen genau dann, wenn auch die Telefonnummern unterschiedlich
# sind. Wir wollen ja nicht, dass die gleiche Person ausversehen mehrfach angerufen
# wird oder wir nicht alle potentiellen Kunden anrufen.
#
# Schreibe eine Funktion 'merge', die zwei Dictionaries miteinander verschmilzt
# und das Telefonbuch nach folgendem Schema ausgibt:
#   |Max Mustermann: 1
#   |Jane Doe: 2
#
# Beschreibe außerdem in einem Kommentar warum die Modellierung der Telefonbücher
# in einem Dictionary im realen Leben keine gute Idee ist (wenn der Name unverändert
# in ein digitales System eingespeist wird, welches Dictionaries nutzt).
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# vielleicht wenn die Namen der Kunden als keys benutzt werden ist es nicht gut, weil mehrere menschen dieselbe Name haben koennten und mit einem Dictionary nur die letzte Person mit dieser Name angerufen werden wird. Falls aber die Nummer als key benutzt werden, dann waere es vielleicht(glaube ich) okay, weil alle Telefonnummer(wenn mit internationalen Code) einzigartig sind und somit keine Probleme entstehen wuerden

def merge(first, second):
    inv_map1 = {v: k for k, v in first.items()}
    inv_map2 = {v: k for k, v in second.items()}
    new = inv_map1 | inv_map2

    return new


phonebook_a = {
    "Max Mustermann": "1",
    "John Doe": "3",
    "Bella Hemmings": "7",
    "Hannah Carter": "8",
    "Eric May": "9",
    "William Sutherland": "10",
    "Jane Doe": "2",
    "Adam Buckland": "4",
    "Winston Churchill": "5",
    "Caroll Brown": "6",
    "Bella Hemmings": "7",
    "Lisa Welch": "11",
    "Theresa Stewart": "12",
}


phonebook_b = {
    "Jane Doe": "2",
    "Adam Buckland": "4",
    "Winston Churchill": "5",
    "Caroll Brown": "6",
    "Bella Hemmings": "7",
    "Lisa Welch": "11",
    "Theresa Stewart": "12",
    "Sue Walker": "13",
    "John Doe": "14",
}

print(merge(phonebook_a, phonebook_b))
