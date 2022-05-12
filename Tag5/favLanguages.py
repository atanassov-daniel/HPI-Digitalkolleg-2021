import csv

with open("programmiersprachen.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    list = list(csv_reader)
    sorted = sorted(list, key = lambda x: x['value'], reverse=True)
    print(sorted)
