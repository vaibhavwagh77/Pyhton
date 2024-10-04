 # def find_string_lenth(strString):
# return (len)




str = 'tables'
str_len = lambda str:len(str)
print(str_len(str))


def addNumber(inum1,inum2):
    return 




print((lambda a,b : a+b)(5,3))





# passsing lambda function as parameter

cube = lambda x : x**3
print(cube(3))


# ============================================================
def my_lambda_function(fun_name,lstNum):
    lstresult = []
    for item in lstNum:
        new_item = fun_name(item)
        lstresult.append(new_item)
        return lstresult
    
lstNum = [2,3,4,5,6]
lstcubed = my_lambda_function(lambda x : x**3,lstNum)
print(lstcubed)


lstNum = [2,3,4,5,6]
lstcubed = map(lambda x : x**3,lstNum)
print(list(lstcubed))



#==============================================================================


print((lambda x,y : " y is greater " if x<y else "x is greater")(5,6))

x = 5
y =6
if x<y:
    print("y is grater")
else:
    print("x is grater")