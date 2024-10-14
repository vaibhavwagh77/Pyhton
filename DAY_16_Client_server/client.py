import socket

#set up the client
client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

#send message to server
# messages=input("Enter the messages you want to send: ")
# client_socket.sendall(messages.encode())
# echoed_message=client_socket.recv(1024).decode()
# print(f"Received from server:  {echoed_message}")

# nums_to_add = input("Enter comma sperated number to add: ")
# client_socket.sendall(nums_to_add.encode())
# echoed_message=client_socket.recv(1024).decode()
# print(f"Received from server:  {echoed_message}")

with open("hiteswari.txt", 'w+') as file:
    while True:
        # Receive data in chunks
        data = client_socket.recv(1024)
        file.write(data)
print('File received successfully.')
#close the client socket
client_socket.close()
print("Connection closed")