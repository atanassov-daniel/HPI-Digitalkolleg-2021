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
from gen_graphs import gen_graphs


def main(chat_path: str):
    results = analyse(chat_path)
    if results.get("no_messages") == True:
        print("There are no messages in the analysed chat")
    else:
        words_used_desc = results.get("words_used_desc")

        lines = []
        words_length = len(words_used_desc)
        end = 0
        if words_length < 100:
            end = words_length
        else:
            end = 100
        for index in range(end):
            lines.append(f"{index + 1}. {words_used_desc[index][0]}")

        from datetime import datetime

        time = datetime.now()
        date = time.astimezone().strftime("%d-%m-%Y_%H-%M-%S")

        # generate info file for the current analysis
        import pathlib

        chat_name = chat_path.split("\\")[-1]
        path = f"output/{date} {chat_name}"
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

        info_sentence = f"This analysis was generated for the file with the path {chat_path} on {date}"

        with open(f"{path}/100_most_common_words.txt", "w", encoding="utf-8") as f:
            f.write(info_sentence + "\n\n")
            f.write("\n".join(lines))
        with open(f"{path}/special_words.txt", "w", encoding="utf-8") as f:
            f.write(info_sentence + "\n\n")
            for i in range(199, 500, 100):
                if i < words_length:
                    f.write(f"{words_used_desc[i][0]} ")

        gen_graphs(
            results.get("people_messages_count_desc"),
            results.get("total_messages"),
            path
        )
        """ print(results.get("people_messages_count_desc"))
        print(results.get("words_used_desc")[:20]) """


from timeit import default_timer as timer

start = timer()
main(
    r"C:\Users\u969672\Downloads\facebook-danielatanassov9\messages\inbox\nqkuvleistungnzelita_weltuy46jw"
)
end = timer()
print(end - start)  # Time in seconds
