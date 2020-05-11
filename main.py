import threading

from camera_stream import webcam_stream

N_CAMS = 1


class camThread(threading.Thread):
    def __init__(self, preview_name, camID):
        threading.Thread.__init__(self)
        self.preview_name = preview_name
        self.camID = camID

    def run(self):
        print("Starting " + self.preview_name + "\n")
        webcam_stream(self.preview_name, self.camID)


if __name__ == "__main__":

    threads = []
    for i in range(N_CAMS):
        threads.append(camThread("webcamera", i))
        threads[i].start()

    print(f'num threads  {threading.active_count()}', threads)
