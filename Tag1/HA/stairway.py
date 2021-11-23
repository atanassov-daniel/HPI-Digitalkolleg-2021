# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# stairway.py
# Eine Treppe mit der Höhe 5 sieht wie folgt aus:
# |
# |    #
# |   ##
# |  ###
# | ####
# |#####
# |
# Deine Aufgabe besteht darin, eine Höhe einzulesen und dann eine Treppe auszugeben.
#
# Tipp: In Python kann man strings durch Multiplikation mit einer Zahl vervielfachen.
#       Außerdem kann man strings mit + zusammenfügen.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

height = int(input("Höhe der Pyramide: "))

for i in range(height):
    num = i + 1
    print(" " * (height - num) + "#" * num)
