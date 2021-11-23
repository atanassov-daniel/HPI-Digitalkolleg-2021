# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# hill.py
# Bei der stairway.py Aufgabe sollst du eine Treppe mit der Höhe 5 wie folgend ausgeben:
#
# |    #
# |   ##
# |  ###
# | ####
# |#####
#
# Ein Hügel mit der Höhe 5 sieht wie folgt aus:
#
# |    # #
# |   ## ##
# |  ### ###
# | #### ####
# |##### #####
#
# Deine Aufgabe besteht darin, eine Höhe einzulesen und den Hügel auszugeben.
#
# Tipp: In Python kann man strings durch Multiplikation mit einer Zahl vervielfachen.
#       Außerdem kann man strings mit + zusammenfügen.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

height = int(input("Höhe des Hügels: "))

""" for i in range(height):
    num = i + 1
    print(" " * (height - num) + "#" * num + " " + "#" * num) """

for i in range(height):
    num = i + 1
    hashtags = "#" * num

    # print(" " * (height - num) + hashtags + " " + hashtags)
    print(f'{" " * (height - num)}{hashtags} { hashtags}')
