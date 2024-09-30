str=input("Enter the String you want to reverse: ")

#str="Hello"
reverse=""
for char in range(len(str)-1, -1, -1):
    reverse +=str[char]


print(reverse)

if(str==reverse):
    print("The strings are identical and same")
else:
    print("The string are not same and identical")
