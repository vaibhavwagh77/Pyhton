import socket
import re
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost',8080)) #Bind to lochahost and port
server_socket.listen(1) #listen for one connection
print("Echo server is lsitening.............")

# recieve the message from the client
client_socket,client_address = server_socket.accept()
# print(f"Connection established with {client_address}")
# client_message = client_socket.recv(1024).decode()
# print(f"Received from server: {client_message}")
# client_socket.sendall(client_message.encode())
client_message=client_socket.recv(1024).decode()
# numlist = client_message.split(",")
# print("Number recieved from server: ",numlist)
# total_sum=0
# for num in numlist:
#     if num != '':
#         total_sum=total_sum+int(num)
# client_socket.sendall(str(total_sum).encode())

#file

with open("hiteshwari.txt", 'r+') as file:
    contents=file.read()
    # Send the file data

    print('File sent successfully.')
client_socket.close()
print("Connection closed")
