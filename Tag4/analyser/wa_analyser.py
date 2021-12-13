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

""" txt = b"\u00d0\u009d\u00d0\u00b5 \u00d1\u0082\u00d1\u0080 \u00d0\u00bb\u00d0\u00b8 \u00d0\u00b4\u00d0\u00b0 \u00d1\u0081\u00d0\u00b8 \u00d1\u0085\u00d0\u00be\u00d0\u00b4\u00d0\u00b8\u00d0\u00bc \u00d0\u00b2\u00d0\u00b5\u00d1\u0087\u00d0\u00b5"

result = txt.decode('unicode-escape').encode('latin1').decode('utf8') """

# * when a chat from Messenger gets exported as a JSON, it contains a object for every single message. Most, but not all messages have a property content with the content of the message itself. For the messages written in Bulgarian an additional step of decoding is needed, in order to fulfill the task, because the message looks something like the following: "\u00d0\u009d\u00d0\u00b5 \u00d1\u0082".
#! this file's function is to decode all the strange looking messages so that future obrabotka of the file is possible
""" txt = "\u00d0\u009d\u00d0\u00b5 \u00d1\u0082\u00d1\u0080 \u00d0\u00bb\u00d0\u00b8 \u00d0\u00b4\u00d0\u00b0 \u00d1\u0081\u00d0\u00b8 \u00d1\u0085\u00d0\u00be\u00d0\u00b4\u00d0\u00b8\u00d0\u00bc \u00d0\u00b2\u00d0\u00b5\u00d1\u0087\u00d0\u00b5"
# txt = "https://vm.tiktok.com/ZM8WJLA7Q/"

result = bytes(txt, "latin-1").decode("utf8")
print(result) """

import json
from pathlib import Path


def main(chat_path: str):
    chat_path = chat_path.replace("\\", "\\\\")

    total_messages = 0
    person_messages = {}
    words_used = {}

    num = 1
    exists = True
    while exists == True:
        my_file = chat_path + f"\\message_{num}.json"
        if Path(my_file).is_file():
            with open(my_file, "r") as f:
                file = json.load(f)
                messages = file["messages"]
                # * the file also includes general info about the chat and its members

                for message in messages:
                    # message is a dict representing a single message
                    if message.get("is_unsent") == False:
                        content = message.get("content")
                        sender = message.get("sender_name")

                        if sender != None:
                            sender = bytes(sender, "latin-1").decode("utf8")
                            total_messages += 1
                            if person_messages.get(sender) == None:
                                person_messages[sender] = 1
                            else:
                                person_messages[sender] += 1

                            # if the message has no content, it just gets ignored
                            if content != None:
                                content = (
                                    bytes(content, "latin-1")
                                    .decode("utf8")
                                    .lower()
                                    .strip()
                                )
                                for word in content.split(" "):
                                    word = word.strip()
                                    # for in the case that words are splitted by a new row and not a space
                                    for wor in word.split("\n"):
                                        if words_used.get(wor) == None:
                                            words_used[wor] = 1
                                        else:
                                            words_used[wor] += 1

            num += 1
        else:
            print(f"The total amount of messages is: {total_messages}")
            person_messages = dict(
                sorted(person_messages.items(), key=lambda item: item[1], reverse=True)
            )
            print(person_messages)
            print("\n")
            print(list(person_messages.items())[:10])
            print("\n")
            print(sorted(person_messages.items(), key=lambda item: item[1], reverse=True)[:10])
            print("\n\n\n")

            words_used = dict(
                sorted(words_used.items(), key=lambda item: item[1], reverse=True)
            )
            print(words_used)
            print("\n")
            print(list(words_used.items())[:20])
            break


from timeit import default_timer as timer

start = timer()
main(
    r"C:\Users\u969672\Downloads\facebook-danielatanassov9\messages\inbox\nqkuvleistungnzelita_weltuy46jw"
)
end = timer()
print(end - start)  # Time in seconds

""" 
#* if for ex. a GIF has been sent, there will be no "content" key, yet it should still count as a message of this sender; I have decided to ignore gifs, because I don't think that it is as likely to get many GIFS that are the same(not exactly sure about that though)
{
    "sender_name": "\u00d0\u009c\u00d0\u00b0\u00d1\u0080\u00d1\u0082\u00d0\u00b8\u00d0\u00bd \u00d0\u0093\u00d0\u00b0\u00d0\u00bd\u00d1\u0087\u00d0\u00b5\u00d0\u00b2",
    "timestamp_ms": 1536956131595,
    "gifs": [
    {
      "uri": "messages/inbox/nqkuvleistungnzelita_weltuy46jw/gifs/31156013_10216241820097849_2881356751293120512_n_521510878319900.gif"
    }
    ],
    "type": "Generic",
    "is_unsent": false
}
{
    "sender_name": "Viktor Angelov",
    "timestamp_ms": 1556634544042,
    "type": "Generic",
    "is_unsent": true
}
"""
