import socket
import sys
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))
print("Connected to server at "+str(port)+" to "+host)
while True:
    k = s.recv(1024)
    print("server->".rjust(170)+k.decode('utf-8'))
    if k.decode() == 'bye':
        s.close()
        sys.exit('bye bye')
    msg = input("messege->server: ")
    s.send(msg.encode('ascii'))
    if msg == 'bye' :
        s.close()
        sys.exit('bye bye')
