import socket

HOST = '172.26.41.138'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)# 5 is the maximum number of queued connections

communication_socket, address = server.accept() #once a connection is accepted this statement runs
print(f"Connected to {address}")
while True:
    
    message = communication_socket.recv(1024).decode('utf-8')# 1024 is the buffer size
    print(f"Message from client is: {message}")

    if message == 'quit':
        communication_socket.close()
        print(f"Connection with {address} ended")

    sender= input("Type your message:")
    communication_socket.send(f"{sender}".encode('utf-8'))
    
    
