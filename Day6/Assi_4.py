#develop the program to manage an inventory system for a small store

dict={}
dict2={}
number=int(input("Enter the how many you want to add: "))
for i in range(number):
    key=input("Enter the item name: ")
    key1=int(input("Enter the item quantity: "))
    value=int(input("Enter the Price: "))
    total=key1*value
    dict2[key1]=total
    dict[key]=dict2
    print(dict)
    choice=input("Do you want to update(p/q): ")
    if(choice=="q"):
        quantity=input("Enter the item quantity: ")
        dict[key]["quantity"]=quantity
        print(dict)
    else:
        if(choice=="p"):
            key=input("Enter the name of item")
        
            price=int(input("Enter the item price: "))
            
            dict[key]["price"]=price
            print(dict)
print(dict)

