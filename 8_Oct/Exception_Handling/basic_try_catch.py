print("demo1: basic try -except block")
try:
    x= int("not_a_number") #this will raise the excption
except ValueError:
    print("caught a vlaue error: Invalid literal for int()")
    
print("\n")