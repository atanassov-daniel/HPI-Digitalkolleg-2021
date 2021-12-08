# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# mapadd.py
#
# Schreibe eine Funktion mapadd, welche eine Zahl entgegen nimmt und diese auf
# jede Zahl in der übergebenen Liste addiert.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def mapadd(number, list):
    for index in range(len(list)):
        list[index] = list[index] + number
    return list

list = mapadd(1, [1, 2, 3, 7, 13, 893, 10000])
print(list)