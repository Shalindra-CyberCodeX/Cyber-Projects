import socket

HOST = '172.26.41.138'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket. SOCK_STREAM)


socket.connect((HOST, PORT))# Connect to server address
while True:
    message = input("Type your message:")
    if message == 'quit':
        break
    else:
        socket.send(message.encode('utf-8'))
        print(socket.recv(1024).decode('utf-8'))# Path: sockets.py
   
