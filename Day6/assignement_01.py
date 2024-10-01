dict1={2:8,3:27,4:64,5:125}
print(dict1)

#To Store the number and the number cubes
dict2={}
number=int(input("Enter the number: "))
for _ in range(number):
    key=int(input("Enter the key value: "))
    dict2[key]= key ** 3
    print(dict2)

