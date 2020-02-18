import socket
import threading
port=8080
address =[]

def Cclinet(c,a):
   rec_data = c.recv(1024)
   print(str(rec_data,'utf-8')," from ",a[0])
   address.remove(a[0])
   if len(address)==0:
       print("No peers are online..")
   else:
        print(len(address)," peers are online..")
   c.close()

def Server():
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.bind(('',port))
   print("Server is initiated and listen to port: ",port)
   sock.listen(5)

   while 1:
      c,a = sock.accept()
      clientThread = threading.Thread(target=Cclinet,args=(c,a))
      clientThread.daemon=True
      clientThread.start()
      address.append(a[0])
      print("Connection ip address ",a[0])
      print(len(address)," peers are online..")
      c.send(bytes(str(len(address)),'utf-8'))
    
   
   sock.close()


Server()