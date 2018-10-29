import pyxhook

class KeyThread():
    def __init__(self, sock=None):
        self.sock=sock
        self.newKeyboard()

    def onKeyPress(self, event):
        print(event.Key)
        print(type(event.Key))
        print(event)
        print(type(event))
        print(event.Ascii)
        print(type(event.Ascii))
        self.sock.send_int_key(event.Ascii)

    def newKeyboard(self):
        self.hook=pyxhook.HookManager()
        self.hook.KeyDown = self.onKeyPress
        self.hook.HookKeyboard()

    def begin(self):
        self.hook.start()

    def keyCancel(self):
        if(self.hook is not None and self.hook.isAlive()):
            self.hook.cancel()
