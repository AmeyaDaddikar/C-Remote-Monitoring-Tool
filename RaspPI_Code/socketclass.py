import socket
import struct

class Mysocket:
	port=9999
	def __init__(self):
		self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.vid=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.mouse=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.key=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print("socket successfully created")
	def connect(self,ip):	
		try:
			self.s.connect((ip,self.port))
			self.vid.connect((ip,self.port+1))
			self.mouse.connect((ip,self.port+2))
			self.key.connect((ip,self.port+3))
		except socket.error as err:
			print("Error occured",err)
	def disconnect(self,discon):
		self.s.sendall(struct.pack('I',discon))
		self.vid.sendall(struct.pack('I',discon))
		self.mouse.sendall(struct.pack('I',discon))
		self.key.sendall(struct.pack('I',discon))
		self.s.close()
		self.vid.close()
		self.mouse.close()
		self.key.close()
	def send_int(self,i):
		self.s.sendall(struct.pack('I',i))
	def send_int_vid(self,i):
		self.vid.sendall(struct.pack('I',i))
	def send_int_mouse(self,i):
		self.mouse.sendall(struct.pack('I',i))
	def send_int_key(self,i):
		self.key.sendall(struct.pack('I',i))
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
