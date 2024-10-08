number=int(input("enter the number"))
student={}
for i in range (number):
    key=(input("Enter the info: "))
    value=input("Enter the value: ")
    student[key]=value


def write_in_dict(filename,my_dict):
    