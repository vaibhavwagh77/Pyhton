from Day_17_Pulgin.pingPlugin.pingPlugin import pingplugin

def main():
    operations={"1":pingplugin()}
    print("choose a network operations:")
    print("1. ping a server")
    print("2. check isd a port is open")
    print("3. resolve a hostname")

    choice= input("Enter the number corresponding to the operation: ")

    if choice not in operations:
        print("Invalid choice!")
        return
    elif choice =="1":
        address= input("Enter the IP address or hostname to ping: ")
        result = operations[choice].execute(address)
    elif choice == "2":
        address = input("Enter the IP address or hostname to ping: ")
        port = int(input("Enter the port number: "))
        result = operations[choice].execute(address,port)

    elif choice == "3":
        hostname = input("Enter the hostname resolve: ")
        result = operations[choice].execute(hostname)

    print(f"Result: {result}")


if __name__=="__main__":
    main()