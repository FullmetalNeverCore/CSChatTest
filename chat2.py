import socket  
import select  
import sys  
from thread import *
  

sver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
  

if len(sys.argv) != 3:  
    print ("use like: chat ip port") 
    exit()  
 
IP_address = str(sys.argv[1])  

Port = int(sys.argv[2])  
 

sver.bind((IP_address, Port))  
  

sver.listen(100)  
  
cl = []  
  
def clientthread(conn, addr):  
  
 
    conn.send("Heya!")  
  
    while True:  
            try:  
                message = conn.recv(2048)  
                if message:  

                    print ("<" + addr[0] + "> " + message)  
  
                    # Calls broadcast function to send message to all  
                    message_to_send = "<" + addr[0] + "> " + message  
                    broadcast(message_to_send, conn)  
  
                else:  

                    remove(conn)  
  
            except:  
                continue

def broadcast(message, connection):  
    for clients in cl:  
        if clients!=connection:  
            try:  
                clients.send(message)  
            except:  
                clients.close()  
  
                # if the link is broken, we remove the client  
                remove(clients)  
  

def remove(connection):  
    if connection in cl:  
        cl.remove(connection)  
  
while True:  

    conn, addr = sver.accept()  
  

    cl.append(conn)  
  
  
    print (addr[0] + " connected") 
  

    start_n_t(clientthread,(conn,addr))    
  
conn.close()  
sver.close()  