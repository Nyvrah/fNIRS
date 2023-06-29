from socket import *
import threading

class Skt(threading.Thread):
    host, port = "127.0.0.1", 25001
    s = socket(AF_INET, SOCK_STREAM)

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        self.s.connect((self.host, self.port))
        print("connecting")

    def send(self, val):
        self.s.send(str(val).encode("utf-8"))
        print("sent")