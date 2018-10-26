from filetransfer import rec_file
from RepeatedTimer import RepeatedTimer

from Tkinter import *

def display_video_data(sc):
    return rec_file(sc, saveFile = False)

def init_video_feed(sc):
    return RepeatedTimer(1,display_video_data, sc)
    
class VideoWindow(Toplevel):
    nid = 0
    #title = "" #this would block the method to override the current title
    message = ""

    def __init__(self, master, nid, title, message,sc):
      Toplevel.__init__(self,master)
      self.nid = nid 
      self.title(title) #since toplevel widgets define a method called title you can't store it as an attribute
      self.message = message
      self.display_note_gui() #maybe just leave that code part of the __init__?
      self.socket_conn = sc

    def display_video_gui(self): 
      '''Tkinter to create a note gui window with parameters '''    
      #no window, just self
      self.geometry("200x200")
      self.configure(background="#BAD0EF")
      #pass self as the parent to all the child widgets instead of window
      title = Entry(self,relief=FLAT, bg="#BAD0EF", bd=0)
      title.pack(side=TOP)
      
      print(display_video_data(self.socket_conn))
      #self.mainloop() #leave this to the root window

    def run(self):
      self.display_video_gui()

