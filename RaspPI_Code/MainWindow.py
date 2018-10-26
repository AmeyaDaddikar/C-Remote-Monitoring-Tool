import tkinter
from socketclass import Mysocket
from filetransfer import *

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
        # self.vid.pack()
        self.root.mainloop()

    def getData(self):
        data = self.entry.get()
        print(data)

    def connections(self):
        sock = Mysocket()
        ip = self.conEntry.get()
        sock.connect(ip)
        self.sock_list.append(sock)
        m = tkinter.Tk()
        # m.mainloop()
        print("Window ready")

    def disconnect(self):
        self.sock_list[self.sock_num].send_int(DISCONNECT)
        self.sock_list[self.sock_num].disconnect()

    def filetransfer(self):
        self.sock_list[self.sock_num].send_int(FILESEND)
        send_file_name(self.sock_list[self.sock_num])
        rec_file(self.sock_list[self.sock_num])

    def choose_socket(self):
        pres_sock = int(input("Enter the number of the socket you want to choose"))
        return(pres_sock - 1)

