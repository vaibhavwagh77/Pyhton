#To create the following keys and accept the user input
dict3={}

number=int(input("Enter the how many you want to add: "))
for i in range(number):
    key="Name"
    value=(input("Enter the Name: "))
    dict3[key]= value
    print(dict3)
    key="Roll_No"
    value1=(input("Enter the Roll_No: "))
    dict3[key]= value1
    key="Science"
    value2=int(input("Enter the Science: "))
    dict3[key]= value2
    key="Maths"
    value3=int(input("Enter the Maths: "))
    dict3[key]= value3
    key="English"
    value4=int(input("Enter the English: "))
    dict3[key]= value4
    print(dict3)
    total=value2+value4+value3
    print(total)
    key="average"
    final_average=int(value2+value4+value3)/3
    dict3[key]= final_average
    print(dict3)

