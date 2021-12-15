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


def analyse(chat_path: str):
    chat_path = chat_path.replace("\\", "\\\\")

    total_messages = 0
    people_messages_count = {}
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
                            if people_messages_count.get(sender) == None:
                                people_messages_count[sender] = 1
                            else:
                                people_messages_count[sender] += 1

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
            if total_messages == 0:
                return {"no_messages": True}
            return {
                "no_messages": False,
                "total_messages": total_messages,
                "people_messages_count": people_messages_count,
                "people_messages_count_desc": sorted(
                    people_messages_count.items(),
                    key=lambda item: item[1],
                    reverse=True,
                ),
                "words_used_desc": sorted(
                    words_used.items(), key=lambda item: item[1], reverse=True
                ),
                
            }


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
