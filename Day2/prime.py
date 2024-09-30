# num=int(input("Enter the range you want of prime number: "))
# i=1
# while i<=num:
#     if (num%i==0 and i%1==0):
#         print(i)
#     i= i+1
   
# Input: A number from the user
number = int(input("Enter a number: "))

# Assume number is prime
is_prime = True

# A number less than 2 is not prime
if number < 2:
    is_prime = False
else:
    # Check for factors from 2 to number-1
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
        print("The number is not prime")

# Output: Whether the number is prime or no
