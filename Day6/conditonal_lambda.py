num=[10,20,-30,-40,50,0,59]

num2=map(lambda x: "zero" if x==0 else "positve" if x>0 else "negative",num)

print(list(num2))