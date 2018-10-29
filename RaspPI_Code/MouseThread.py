import threading
from Xlib import display
from StoppableThread import StoppableThread

class MouseThread(StoppableThread):
    def __init__(self, threadName, sock=None):
        super().__init__(threadName)
        self.sock=sock
    def run(self):
        while(not self.stopped()):
            data = display.Display().screen().root.query_pointer()._data
            self.sock.send_int_mouse(2)
            self.sock.send_int_mouse(data["root_x"])
            self.sock.send_int_mouse(data["root_y"])
