import tkinter

from MouseThread import MouseThread
from KeyThread import KeyThread
from socketclass import Mysocket
from filetransfer import *
from mousepos import *
from keyboard import *

DISCONNECT=0
FILESEND=1

class MainWindow:
    def __init__(self):
        self.sock_num = -1
        self.sock_list = []
        self.root = tkinter.Tk()
        self.disc = tkinter.Button(self.root, text="Disconnect", command=self.disconnect)
        self.file = tkinter.Button(self.root, text="Receive File", command=self.filetransfer)
        self.con = tkinter.Button(self.root, text="Connect", command=self.connections)
        self.ch = tkinter.Button(self.root, text="Change Connection", command=self.choose_socket)
        # self.vid = tkinter.Button(self.root, text="Video Feed", command=feed)
        self.fileEntry = tkinter.Entry(self.root)
        self.conEntry = tkinter.Entry(self.root)
        self.chEntry = tkinter.Entry(self.root)
        self.disc.pack()
        self.fileEntry.pack()
        self.file.pack()
        self.conEntry.pack()
        self.con.pack()
        self.chEntry.pack()
        self.ch.pack()
        self.mouseThread = MouseThread("MouseThread")
        self.keyThread = KeyThread()
        # self.vid.pack()

        self.root.mainloop()

    def getData(self):
        data = self.entry.get()
        print(data)

    def setSock(self, sock_num):
        self.sock_num = sock_num
        self.mouseThread.stop()
        if(self.mouseThread is not None):
            self.mouseThread = MouseThread("MouseThread", self.sock_list[sock_num])
        self.mouseThread.start()
        if(self.keyThread is not None):
            self.keyThread.keyCancel()
        self.keyThread = KeyThread(self.sock_list[sock_num])
        self.keyThread.begin()

    def connections(self):
        sock = Mysocket()
        ip = self.conEntry.get()
        sock.connect(ip)
        self.sock_list.append(sock)
        self.setSock(len(self.sock_list) - 1)
        m = tkinter.Tk()
        # m.mainloop()
        print("Window ready")

    def disconnect(self):
        self.sock_list[self.sock_num].disconnect(DISCONNECT)

    def filetransfer(self):
        self.sock_list[self.sock_num].send_int(FILESEND)
        file_name = self.fileEntry.get()
        send_file_name(self.sock_list[self.sock_num], file_name)
        rec_file(self.sock_list[self.sock_num], "OK")

    def choose_socket(self):
        pres_sock = self.chEntry.getint()
        self.setSock(pres_sock - 1)

