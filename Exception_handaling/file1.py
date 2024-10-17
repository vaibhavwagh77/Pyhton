#Basic try_except block
print("Demo 1: Basic try-except block")
try:
    x=int("not_a_no")
except ValueError:
    print("Cought a ValueError: Invalid literal for int()")


    print("\n")



     #Multiple except blocks(handling different exception separately
print("Demo 2: Basic try-except block")
try:
    x=int(input("Enter a number: "))
    y=x/5
    print(y)
except ValueError:
    print("Cought a ValueError")
except ZeroDivisionError:
    print("Cought a ZeroDivisionError: Division by zero is not allowed")

    print("\n")


#try except-finally block
print("Demo 3 : Try-except-finally block")
try:
    z= 10/5
except ZeroDivisionError :
    print("caught a ZeroDivisionError: Division by zero is not allowed")
finally:
    print("This will always execution occurred")
print("\n")

#Raising an exception
print("Demo 4: Raising an exception")
try:
    age = -1
    if age < 0:
        raise ValueError("Age cannot be Negative")
except ValueError as e:
    print(f"Raised and caught exception: {e}")


#DEMO 5
print("Demo 5: Raising an exception")
try:
    age = -1
    amount = -1
    if age < 0:
        raise ValueError("Age cannot be Negative")
    if amount < 0:
        raise ValueError("Amount cannot be Negative")

except ValueError as e:
    print(f"Raised and caught exception: {e}")

#