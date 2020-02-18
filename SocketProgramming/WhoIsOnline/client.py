import socket
import time

host ="127.0.0.1"
port = 8080

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start_time = time.time()
    sock.connect((host,port))
    end_time = time.time()
    print("RTT = ",end_time-start_time)
    peer_data = sock.recv(1024)
    print(str(peer_data,'utf-8')," peers are online..")
    print("To exit enter any key")
    sns_data = input()
    sock.send(bytes("Disconnected ",'utf-8'))
    sock.close()

client()