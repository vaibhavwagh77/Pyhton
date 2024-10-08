def get_integer_input(num):
    print(num)
    
number=int(input("Enter the number: "))
get_integer_input(number)

try:
    if number <0:
        raise ValueError("the number is greater than 0")
except ValueError as e:
    print("the number is smaller than 0")
    
    
#def get_element_from_list(num):

# def divide_number(a,b):
#     ans=(a%b)
#     print(ans)
#     return ans
#     try:
#         if b==0:
#             raise ZeroDivisionError("cannot perform the operation")
#     except ZeroDivisionError as e:
#         print("the number is not divisible by zero")


# num1=2
# num2=0
# divide_number(num1,num2)




def divide_number(a,b):
    if b==0:
        raise ZeroDivisionError("Division by zero")
    ans=(a%b)
    return ans
try:
    result=divide_number(2,0)
except ZeroDivisionError as e:
        print("the number is not divisible by zero")


