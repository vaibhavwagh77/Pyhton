number=int(input("Enter a number: "))
prime_numbers=[]
for i in range(2,number+1):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        prime_numbers.append(i)
print(prime_numbers)