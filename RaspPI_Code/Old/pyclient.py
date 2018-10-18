import socket
import struct
import sys
from Xlib import display

DISCONNECT = 0
FILESEND = 1
MOUSEMOVE = 2
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.43.236",9999))

f = open('index.jpeg', 'rb')
content = f.read()

size = len(content)
print size
print struct.pack('I', size)

s.sendall(struct.pack('i', FILESEND))
s.sendall(struct.pack('i', size))
print(sys.getsizeof(struct.pack('i', size)))
s.sendall(content)
data = display.Display().screen().root.query_pointer()._data
s.sendall(struct.pack('i', MOUSEMOVE))
s.sendall(struct.pack('i', data["root_x"]))
s.sendall(struct.pack('i', data["root_y"]))
s.sendall(struct.pack('i', DISCONNECT))


