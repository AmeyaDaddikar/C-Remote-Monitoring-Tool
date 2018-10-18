from socketclass import Mysocket

def send_file_name(sc):
    temp=raw_input("enter the file name u want")
    print(temp)
    sc.send_int(len(temp))
    sc.send(temp)

def rec_file(sc):
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
    name = raw_input("Enter the name you want to save with")
    tempfile=open(name,"wb")
    tempfile.write(total_contents)
