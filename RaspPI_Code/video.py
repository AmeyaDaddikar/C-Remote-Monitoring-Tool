from filetransfer import rec_file
from RepeatedTimer import RepeatedTimer

from tkinter import *

def display_video_data(sc):
    return rec_file(sc, saveFile = False)

def init_video_feed(sc):
    return RepeatedTimer(1,display_video_data, sc)
    
class VideoWindow(Toplevel):
    nid = 0
    #title = "" #this would block the method to override the current title
    message = ""

    def __init__(self, master,sc):
      Toplevel.__init__(self,master)
      self.display_note_gui() #maybe just leave that code part of the __init__?
      self.socket_conn = sc

    def display_video_gui(self): 
      '''Tkinter to create a note gui window with parameters '''    
      #no window, just self
      self.geometry("600x600")
      self.configure(background="#BAD0EF")
      #pass self as the parent to all the child widgets instead of window
    #   title = Entry(self,relief=FLAT, bg="#BAD0EF", bd=0)
    #   title.pack(side=TOP)
      
      print(display_video_data(self.socket_conn))
      #self.mainloop() #leave this to the root window

    def run(self):
      self.display_video_gui()

