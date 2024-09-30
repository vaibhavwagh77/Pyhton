for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()


for i in range(1,6+1):
    for j in range(6-i):
        print(" ", end=" ")
    for k in range (1,i+1):
        print(" * ",end=" ")
    print()

i=1
while i<=5: 
    j=1
    while j<=i:
        print(i, end=" ")
        j+=1
    print()
    i+=1