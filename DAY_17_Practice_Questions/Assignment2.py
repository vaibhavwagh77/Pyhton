def reverse(lsit):
    return list[::-1]

def larger_number(list):
    large=max(list)
    small=min(list)
    return large,small


list=[100,200,300,400,500]
second_list=reverse(list)
print(f"The real the lis is {list}")
print(f"The reverse list is {second_list}")
large,small=larger_number(list)
print(f"The larger Number is: {large}\nThe Smaller Number is: {small}")


