from tkinter import *
import threading

class Win(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
    
    def end(self):
        self.root.quit()

    def run(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.end)
        self.s = Scale(self.root, from_=2250, to=3000, length=600, tickinterval=30)
        self.s.pack()
        mainloop()
    
    def update(self, val):
        self.s.set(val)