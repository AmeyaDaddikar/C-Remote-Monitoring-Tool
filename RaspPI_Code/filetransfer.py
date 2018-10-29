from socketclass import Mysocket

def send_file_name(sc,temp):
    print(temp)
    sc.send_int(len(temp))
    sc.send(temp.encode())

def rec_file(sc, name, saveFile = True):
    print("Here")
    size = sc.receiveint()
    total_size = 0
    total_contents = ""
    while True:
        recv_size = min(1, size - total_size)
        if(recv_size <= 0):
            print("Done")
            break
        print("Receiving")
        data=sc.receivebyte(recv_size)
        print("Received")
        total_size = total_size + recv_size
        if not data:
            print("No data")
            break
        print(data)
        total_contents += data
    
    if saveFile:
        # name = raw_input("Enter the name you want to save with")
        tempfile=open(name,"wb")
        tempfile.write(total_contents)
        return
    
    return total_contents
