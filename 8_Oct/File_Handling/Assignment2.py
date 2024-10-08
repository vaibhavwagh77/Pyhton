import csv
a="a.txt"


with open(a, 'r') as file:
        # Read the content of the file
        file_content = file.read()
        print(file_content)