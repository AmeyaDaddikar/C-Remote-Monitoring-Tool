import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
print(host)
s.connect((host, port))

while True:
       x=s.recv(1024)
       print(x)
       if x=="1":
              name=s.recv(1024)
              
              temp=open("/home/161070055/Desktop/tp","rb")
              flag=True
              while flag:
                     data=temp.readline()
                     if not data:
                            flag=False
                     print(data)
                     s.send(data)
                     
              temp.close()
              s.close()
              break
