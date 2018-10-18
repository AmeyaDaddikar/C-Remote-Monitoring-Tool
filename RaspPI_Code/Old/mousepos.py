from Xlib import display
while True:
    data = display.Display().screen().root.query_pointer()._data
    print "The mouse position on the screen is",data["root_x"], data["root_y"]
