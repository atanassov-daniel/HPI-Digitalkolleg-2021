# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# wa_analyser.py
# Heute implementierst du den ersten Teil deines Endprojektes, einen Script welches einen WhatsApp
# Chat analysiert. Folge zunächst diesen Schritten:
#   1. Exportiere deinen ChatsApp Chat (ohne Medien)!
#   2. Nimm die .txt Datei und bewege Sie in den Ordner in dem auch dieses Script liegt.
# Nun schreibe ein Python Programm welches diese Datei einliest und basierend
# darauf Infographiken zu folgenden Fragen erstellt.
#
#  1. Welche sind die 100 meistverwendeten Wörter?
#       -> Ausgabe in die Datei 100_most_common_words.txt
#               |1. ich
#               |2. der
#               |...
#  2. Welches ist das 200., 300., 400. und 500. meistverwendete Wort?
#       -> Ausgabe in die Datei special_words.txt, getrennt mit einem Leerzeichen.
#  3. Wie viele Nachrichten hat jede Person geschrieben?
#       -> Bar Chart
#  4. Wie hoch liegt der prozentuale Anteil?
#       -> Pie Chart
# Für Fortgeschrittene:
#  5. In welcher Stunde vom Tag wart ihr am aktivsten?
#       -> Line Chart
#  6. In welcher Stunde vom Tag war jede Person am aktivsten?
#       -> Line Chart
# Anmerkung: Großbuchstaben sollen zu Kleinbuchstaben transformiert werden.
#
# Um diese Graphen zu erzeugen musst du mehrere Funktionen schreiben, am Ende
# soll das Program durch den Aufruf der Funktion main alle Inforgrafiken generieren.
#
# |def main(filepath: str):
# |    # ...
# |
# |main("wa_chat_with_my_bff.txt")
#
# Um diese Aufgabe bewältigen zu können, empfehlen wir euch die Dokumentation von Plotly anzugucken.
#       Bar Chart - https://plotly.com/python/bar-charts/
#       Pie Chart - https://plotly.com/python/pie-charts/
#       Line Chart - https://plotly.com/python/line-charts/
#
# Viel Spaß und viel Erfolg. Bei Fragen (welche absolut verständlich sind, denn das hier ist alles andere als eine triviale
# Aufgabe), stehen wir euch gerne zur Seite!
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from analyse import analyse

def main(chat_path: str):
    results = analyse(chat_path)
    if results.get("no_messages") == True:
        print("There are no messages in the analysed chat")
    else:
        print(f"The total amount of messages is: {results.get('total_messages')}")
        print(results.get("people_messages_count_desc"))
        print(results.get("words_used_desc")[:20])


from timeit import default_timer as timer

start = timer()
main(
    r"C:\Users\u969672\Downloads\facebook-danielatanassov9\messages\inbox\nqkuvleistungnzelita_weltuy46jw"
)
end = timer()
print(end - start)  # Time in seconds
