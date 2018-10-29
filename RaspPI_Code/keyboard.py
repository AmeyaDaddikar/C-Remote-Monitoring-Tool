import sys, tty, termios
def get_key(sock):    
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    #print "hhfeih"
    try:
        while True:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if(ch == '\n'):
                break
            print(ch)
            sock.send_int(ord(ch))
    finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

