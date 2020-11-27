import socket
import sys    
import select  

  
sver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
if len(sys.argv) != 3:  
    print ("use like: chat ip port") 
    exit()  
IP = str(sys.argv[1])  
Port = int(sys.argv[2])  
sver.connect((IP, Port))  
  
while True:  
  
    sockets_list = [sys.stdin, sver]  
  
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])  
  
    for socks in read_sockets:  
        if socks == sver:  
            message = socks.recv(2048)  
            print (message)  
        else:  
            message = sys.stdin.readline()  
            sver.send(message)  
            sys.stdout.write("You :")  
            sys.stdout.write(message)  
            sys.stdout.flush()  
sver.close()  