import csv
with open('words.csv',mode='r',encoding='utf-8') as file:
    reader= csv.reader(file)
    print(reader)
    for row in reader: #read data from csv file in the list
        words=row
    sorted_words = sorted(words)
    print(sorted_words)
with open('sorted.csv',mode='w',encoding='utf-8') as file:
    writer= csv.writer(file)
    print("Data added")
    writer=csv.writer(sorted_words)

