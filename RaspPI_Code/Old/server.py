import socket               # Import socket module

def choose(items,x):
       print(x)
       for c,name in items:
              print(c,name)
              if x==c:
                   print(c)
                   return name
       return None
       
def closeconn(item):
       for c,name in item:
              name.close()

def conn():
       global sc
       flag=True
      
       while flag:
       
              x=input("enter the name of pc")
       
              sc = choose(portTable.items(),x)
              print(sc)             
              n=input("press 1 if u want to receive data else press any number")
              print(n)
              while n==1:
                     sc.send("1")
                     
                     temp=raw_input("enter the file name u want")
                     print(temp)
                     sc.send(temp)
                     
                     tempfile=open(temp,"wb")
                     flag2=True
                     while flag2:
                     
                            data=sc.recv(1048)
                            print(data)
                            if not data:
                                   flag2=False
                     
                            tempfile.write(data)
                     
                     n=input("press 1 if want to receive more data otherwise press any number")
                     
              fl=raw_input("press f if u want to stop otherwise press t")
              if fl=='f':
                     flag=False
                     closeconn(portTable.items())
              else:
                     flag=True


def main():
       global portTable
       s = socket.socket()         # Create a socket object
       s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       host = socket.gethostname() # Get local machine name

       port = 12345                # Reserve a port for your service.

       s.bind((host, port))        # Bind to the port

       print("hello")

       s.listen(5) 

       print("hello")               # Now wait for client connection.

       portTable={}

       i=0
       while i<1:
          c, addr = s.accept()     # Establish connection with client.
          print(addr)
          portTable.update({addr[1] : c})
          
          i=i+1
             
       conn()   
       
if __name__=="__main__":
       main()
