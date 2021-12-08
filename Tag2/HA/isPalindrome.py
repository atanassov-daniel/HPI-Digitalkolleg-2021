# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# isPalindrome.py
#
# Schreibe eine Funktion is_palindrome, welche überprüft ob eine Zeichenkette ein
# Palindrom ist. Die Funktion muss außerdem einen Docstring haben.
# Ein Palindrom ist eine Zeichenkette die vorwärts wie rückwärts gleich zu lesen
# ist. Achtung: Groß- oder Kleinschreibung ist hierbei irrelevant. Du kannst dir
# die Aufgabe also einfacher machen indem du alle Buchstaben in Groß- oder
# Kleinbuchstaben umwandelst. Google dazu welche Funktionen Python bereitstellt.
# Überlege wie du eine leere Zeichenketten behandelst.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def is_palindrome(string):
    if len(string) == 0:
        return "empty string"

    string = string.lower()
    if string[::-1] == string:
        return True
    else:
        return False


# Test your code
# True:
print(is_palindrome("netten"))
print(is_palindrome("Anna"))
print(is_palindrome("Otto"))
print(is_palindrome("s"))
print(is_palindrome(""))
print(is_palindrome("Salas"))
print(is_palindrome("Teebeet"))
print(is_palindrome("WOW wOw woW Wow"))

# False:
print(is_palindrome("Harry"))
print(is_palindrome("Hermine"))
print(is_palindrome("Ron"))
print(is_palindrome("Dumbledore"))
print(is_palindrome("+-"))
print(is_palindrome("Oww"))
print(is_palindrome("abccdcba"))
print(is_palindrome("abc d cba "))