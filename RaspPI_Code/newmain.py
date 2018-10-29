from socketclass import Mysocket
from filetransfer import *
from keyboard import *
from mousepos import *
from video import init_video_feed
import tkinter
from MainWindow import MainWindow as mw

# MOUSE_MOVE=2

def display_options():
    print("Enter one of the options:")
    print("1) DISCONNECT")
    print("2) FILE RECIEVE")
    print("3) CONNECT")
    print("4) CHANGE CONNECTED PC")
    print("5) VIDEO (debugging)")

    choice = int(input("Enter the option number"))
    return(choice - 1)

def keyboardcontrol(sock_num):
    get_key(sock_list[sock_num])

def mousecontrol(sock_num):
    sock_list[sock_num].send_int(MOUSE_MOVE)
    mouse_move(sock_list[sock_num])


sock_list = []

m = mw()
