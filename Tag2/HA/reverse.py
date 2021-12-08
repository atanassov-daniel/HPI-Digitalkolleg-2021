# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# reverse.py
#
# Schreibe eine Funktion reverse, welche einen string in umgekehrter Reihenfolge
# zurückgibt. Den string sollst Du dir von Nutzer holen und den umgedrehten String
# auch wieder zurückgeben.
# Im gesamten Programm dürfen ausschließlich die Funktionen len, print
# und input genutzt werden.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

string = input("Please input your string: ")

new = ""
for i in range(len(string) - 1, -1, -1):
    new += string[i]
print(new)

# ik6ip >>> pi6ki   # "  pk p"
