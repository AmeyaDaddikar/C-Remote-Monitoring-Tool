from socketclass import Mysocket
from filetransfer import *
from keyboard import *
from mousepos import *

DISCONNECT=0
FILESEND=1
MOUSE_MOVE=2

def display_options():
    print("Enter one of the options:")
    print("1) DISCONNECT")
    print("2) FILE RECIEVE")
    print("3) MOUSE CONTROL")
    print("4) KEYBOARD")
    print("5) CONNECT")
    print("6) CHANGE CONNECTED PC")
    choice = int(input("Enter the option number"))
    return(choice - 1)

def connections():
    sock = Mysocket()
    ip = raw_input("Enter IP address")
    sock.connect(ip)
    sock_list.append(sock)

def disconnect(sock_num):
    sock_list[sock_num].send_int(DISCONNECT)
    sock_list[sock_num].disconnect()

def filetransfer(sock_num):
    sock_list[sock_num].send_int(FILESEND)
    send_file_name(sock_list[sock_num])
    rec_file(sock_list[sock_num])

def keyboardcontrol(sock_num):
    get_key(sock_list[sock_num])

def mousecontrol(sock_num):
    sock_list[sock_num].send_int(MOUSE_MOVE)
    mouse_move(sock_list[sock_num])
    
def choose_socket():
    pres_sock = int(input("Enter the number of the socket you want to choose"))
    return(pres_sock - 1)

sock_list = []

while True:
    choice = display_options()
    if(choice == 0):
        disconnect(pres_sock)
    elif(choice == 1):
        filetransfer(pres_sock)
    elif(choice == 2):
        mousecontrol(pres_sock)
    elif(choice == 3):
        keyboardcontrol(pres_sock)
    elif(choice == 4):
        connections()
    elif(choice == 5):
        pres_sock = choose_socket()
