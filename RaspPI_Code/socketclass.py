import socket
import struct

class Mysocket:
	port=9999
	def __init__(self):
    		self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print "socket successfully created"
	def connect(self,ip):	
		try:
                        self.s.connect((ip,self.port))
		except socket.error as err:
			print "Error occured",err
	def disconnect(self):
		self.c.close()
	def send_int(self,i):
		self.s.sendall(struct.pack('I',i))
	def send(self,str):
                self.s.sendall(str)
	def sendbyte(self):
		my_bytes = bytearray()
		byte_input=input("Enter")
		while byte_input: 
			my_bytes.append(byte_input)
			byte_input=input()
	def receivebyte(self, size):
                print("Getting")
		self.data=self.s.recv(size)
		print(self.data)
		return self.data
	def receiveint(self):
                data = self.receivebyte(4)
                str_data = data[::-1]
                power = 1
                size = 0
                for c in str_data:
                        size = size + ord(c) * power
                        power = power * 256
                return size
