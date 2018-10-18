from Xlib import display

def mouse_move(s):
    data = display.Display().screen().root.query_pointer()._data
    s.send_int(data["root_x"])
    s.send_int(data["root_y"])
