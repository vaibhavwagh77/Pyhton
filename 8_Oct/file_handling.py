#list of the random number

list=[1,2,3,4,5,6,7,9]

with open ("numbers1.txt","w") as f:
    for i in range (len(list)):
        f.write(f"{list[i]}\n")
    
    
f= open("numbers1.txt","r")
data=f.read()
print(data,sep="\n")
f.close()

for i in range (len(data)):
    count=0
    sum=count + i
    i=+1
    print(sum)