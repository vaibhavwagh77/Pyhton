def processnumber(num1,num2=5):
    resultAdd= num1+num2
    resultmul= num1*num2
    return resultAdd,resultmul


num1=int(input("Enter the number first: "))
num2=int(input("Enter the number second: "))

result=processnumber(num1)
print(result)