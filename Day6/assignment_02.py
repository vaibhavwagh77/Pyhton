#To assign the ascii the value in the dict3
dict3={}
number=int(input("Enter the how many you wnat to add: "))
for _ in range(number):
    key=(input("Enter the key value(char): "))
    dict3[key]= ord(key)
    print(dict3)