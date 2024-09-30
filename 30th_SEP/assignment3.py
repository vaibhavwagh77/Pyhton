tupel=[]
inputs=input("Enter the tuple elements: ")
tupel=inputs.split(',')
print(tuple)
tupel2=tuple(tupel)
print(tupel2)
#SUM OF THE VALUE IN THE TUPLE:
# i=0
# count=0
# for i in tupel2:
#     count = i+1
# print(count)


t2=(sorted(tupel2))
print(t2)
t3=tuple(t2)

threshold=int(input("Enter the value: "))

for i in t3:
    if(int(i)>threshold):
        print("the element is greater")
    else:
        print("the element is not greater")