name=input("Enter the name of the user: ")
age=int(input("Enter the age of the user: "))
list1=[name,age]
t11=(name,age)
print(t11)
print(list1)
print(type(list1))
tuple2=tuple(list1)
print(tuple2)
a,b=tuple2
print(a)
print(b)