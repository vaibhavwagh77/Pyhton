ch1 = "y"
while ch1 == "y":
    num1 = int(input("enter the first no"))
    num2 = int(input("enter the scond no"))

    ch="y"
    while ch == "y":
        x = input("enter operation")
        if x=="+":
            print("addition of {} & {} is " . format(num1,num2), num1+num2)
        elif  x=="-":
            print("sub of {} & {} is " . format(num1,num2), num1-num2)
        elif  x=="*":
            print("mul of {} & {} is " . format(num1,num2), num1*num2)
        elif  x=="/":
            print("div of {} & {} is ".format(num1, num2), num1 / num2)
        ch=input("do you want to perfrom the operation? [y/n]")
        ch1=input("do you want to change the no?[y/n]")