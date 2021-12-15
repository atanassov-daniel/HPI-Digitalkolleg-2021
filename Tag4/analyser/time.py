from datetime import datetime

x = datetime.now()

print(x.astimezone().strftime("%d-%m_%Y-%H:%M:%S"))
# print(x)