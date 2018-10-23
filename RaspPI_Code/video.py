from filetransfer import rec_file
from RepeatedTimer import RepeatedTimer

def display_video_data(sc):
    image_data = rec_file(sc, saveFile = False)
    print(image_data[0])
def init_video_feed(sc):
    return RepeatedTimer(1,display_video_data, sc)
    

