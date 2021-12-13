""" txt = b"\u00d0\u009d\u00d0\u00b5 \u00d1\u0082\u00d1\u0080 \u00d0\u00bb\u00d0\u00b8 \u00d0\u00b4\u00d0\u00b0 \u00d1\u0081\u00d0\u00b8 \u00d1\u0085\u00d0\u00be\u00d0\u00b4\u00d0\u00b8\u00d0\u00bc \u00d0\u00b2\u00d0\u00b5\u00d1\u0087\u00d0\u00b5"

result = txt.decode('unicode-escape').encode('latin1').decode('utf8') """

#* when a chat from Messenger gets exported as a JSON, it contains a object for every single message. Most, but not all messages have a property content with the content of the message itself. For the messages written in Bulgarian an additional step of decoding is needed, in order to fulfill the task, because the message looks something like the following: "\u00d0\u009d\u00d0\u00b5 \u00d1\u0082". 
#! this file's function is to decode all the strange looking messages so that future obrabotka of the file is possible
txt = "\u00d0\u009d\u00d0\u00b5 \u00d1\u0082\u00d1\u0080 \u00d0\u00bb\u00d0\u00b8 \u00d0\u00b4\u00d0\u00b0 \u00d1\u0081\u00d0\u00b8 \u00d1\u0085\u00d0\u00be\u00d0\u00b4\u00d0\u00b8\u00d0\u00bc \u00d0\u00b2\u00d0\u00b5\u00d1\u0087\u00d0\u00b5"
# txt = "https://vm.tiktok.com/ZM8WJLA7Q/"

result = bytes(txt, "latin-1").decode("utf8")
print(result)

import json

with open("message_1.json", "r") as f:
    file = json.load(f)
    messages = file["messages"] #* the file also includes general info about the chat and its members
   
    for message in messages: # message is a dich representing a single message
        content = message.get("content")
        if  content!= None: #if the message has no content, it just gets ignored
            print(content)
            break

#! I have to then somehow edit this things into the json file