import os
from datetime import datetime as dt
import win
import skt

w = win.Win()
s = skt.Skt()

def start():
    folder = "data/" + os.listdir('data')[0] + "/"
    f = [f for f in os.listdir(folder) if f.endswith('.nir')][0]
    file = open(folder + f, "r")
    for _ in range(14):
        line = new(file)
    run(line, dt.now(), len(line)-2, file)

def run(line, i, n, file):
    while True:
        d = time(i)
        if d >= float(line[0]):
            a = avg(line, n)
            w.update(a[0])
            s.send(a[0])
            print(a)
            line = new(file)
            if line[0] == '-1':
                break

def new(file):
    return file.readline().split()

def time(i):
    return round((dt.now() - i).total_seconds(),3)

def avg(line, n):
    avg = [0,0,0]
    for i in range(1, n+1):
        avg[i%3-1] += int(float(line[i])/(n/3))
    return avg