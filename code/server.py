import socket
import sys
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)
print("Sever is listning for clients at "+str(host)+":"+str(port))
while True:
    c,addr = s.accept()
    print("Got Connection from\nhostname =  ",addr[0],"\nPort = ",addr[1])
    print("\n\n")
    while True:
        msg = input("Messege->client: ")
        c.send(msg.encode('ascii'))
        if msg == 'bye' :
            c.close()
            sys.exit("bye bye")
        m = c.recv(1024)
        print("client->".rjust(170),m.decode())
        if  m.decode() == 'bye' :
            c.close()
            sys.exit("Bye Bye ")
            






