# a=int(input)
# list=[]

items = []
inputs = input("Enter elements separated by commas: ")
items=inputs.split(',')
print("Your list:", items)

tuple1=tuple(items)
print("The Tuple is",tuple1)

#find the first element of th tuple

print(tuple1[0])
#find the last element of th tuple
print(tuple1[-1])
#only print the tuple exceluding first and last element
lenght=len(tuple1)
print(tuple1[1:lenght-1])
#only print the 2nd number and then second number of the tuple
print(tuple1[1:lenght-1:2])

#revrse the tuples
print(tuple1[::-1])


