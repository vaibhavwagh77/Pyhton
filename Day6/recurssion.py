def recursive_sum(number):
    print(number)
    '''base case: if the luse is empty, return 0'''
    if not number:
        return 0
    else:  '''recursuve case: add the first number to the sum id the rest'''
    return number[0] + recursive_sum(number[1:])
    





number=[1,2,3,4,5]
result= recursive_sum(number)
print(result)