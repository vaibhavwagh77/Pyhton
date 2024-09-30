list1=[]
while True:
    print()
    print("1. Add task to list")
    print("2. Remove task from list")
    print("3. Display list")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        task=(input("Enter a task: "))
        list1.append(task)
    elif choice==2:
        task=(input("Enter a task to remove: "))
        if task in list1:
            list1.remove(task) 
        else:
            print("task not found in the list")
    elif choice==3:
        print(list1)
    elif choice==4:
        break
    else:
        print("Invalid choice")