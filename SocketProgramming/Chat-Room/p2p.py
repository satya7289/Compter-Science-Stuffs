from random import randint
import sys
import socket
import threading
import time

Buffer = 1024
Port = 8888
"""
class Peer to store the list of address(IP) of the all peers. At initial it is ['127.0.0.1']
"""
class Peer:
    peer =['127.0.0.1']
"""
class Server is to create a server and use thread for diffrent client
"""
class Server:
    '''
    connections are list of connections that are present in the network.
    peers are list of address of each peer in the network.
    Server class has of constructor for created or accepting connections.
    handleClient is used for handling each peers(thread)
    peerConnectionMess is used for send new  peers are connected in the network.
    broadcastMessage is used for send brodcast that new peers is connected.
    '''
    Connections =[]
    Peers =[]
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('',Port))
        sock.listen(1)
        print("Server is started... Listening to port : ",Port)
        while True:
            client,address     = sock.accept()
            clientTread        = threading.Thread(target=self.handleClient,args=(client,address))
            clientTread.daemon =True
            clientTread.start()
            self.Connections.append(client)
            self.Peers.append(address[0])
            self.peerConnectionMess()
            self.broadcastMess(1,address)
            print("Got connection from "+str(address[0])+" on port :"+str(address[1]))

    def handleClient(self,client,address):
        while True:
            rec_data = client.recv(Buffer)
            for conection in self.Connections:
                conection.send(rec_data)
            if not rec_data:
                print("Got disconnection from "+str(address[0])+" on port :"+str(address[1]))
                self.broadcastMess(0,address)
                self.Connections.remove(client)
                self.Peers.remove(address[0])
                self.peerConnectionMess()
                client.close()
                break

    def peerConnectionMess(self):
        p = ""
        for peer in self.Peers:
            p = p + peer +','
        for connection in self.Connections:
            connection.send(b'\x11'+bytes(p,'utf-8'))
    
    def broadcastMess(self,status,address):
        if status==1:
            message = "Got connection from "+str(address[0])+" on port :"+str(address[1])
        else:
            message = "Got disconnection from "+str(address[0])+" on port :"+str(address[1])
        for connection in self.Connections:
            connection.send(b'\x12'+bytes(message,'utf-8'))


class Client:
    '''
    Client class has of constructor used for connected into the network.
    sendMessage is used sending message to all peers(thread)
    updatePeer is used for updating peers address.
    '''
    def __init__(self, address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        start_time = time.time()
        sock.connect((address,Port))
        end_time = time.time()
        print("Round Trip time: ",end_time-start_time)
        inputThread = threading.Thread(target=self.sendMessage,args=(sock,))
        inputThread.daemon=True
        inputThread.start()
        while True:
            rec_data = sock.recv(Buffer)
            if not rec_data:
                break
            if rec_data[0:1]==b'\x11':
                self.updatePeer(rec_data[1:])
            elif rec_data[0:1]==b'\x12':
                print(str(rec_data[1:],'utf-8'))
            else:
                print(str(rec_data,'utf-8'))

    def sendMessage(self,sock):
        while True:
            sock.send(bytes(input(""),'utf-8'))
    
    def updatePeer(self,data):
        Peer.peer = str(data,'utf-8').split(",")[:-1]
        print(Peer.peer)
        print(len(Peer.peer)," Peers are online now...")


'''
For Creating peers first starting any server using default address '127.0.0.1'.
and then for each peer make them as client as well as server both.
if keyboardInterrupt then exit from the code.
'''

while  1:
    try:
        print("Trying to connect...")
        time.sleep(randint(1,5))
        for peer in Peer.peer:
            try:
                client = Client(peer)
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                pass
            try:
                server = Server()
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                print("Could not able to connect")
    except KeyboardInterrupt:
        sys.exit(0)
    
