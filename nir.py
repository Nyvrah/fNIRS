import os
from datetime import datetime as dt

folder = "data/" + os.listdir('data')[0] + "/"
f = [f for f in os.listdir(folder) if f.endswith('.nir')][0]
file = open(folder + f, "r")

def new():
    return file.readline().split()

def time(i):
    return (dt.now() - i).total_seconds()

def avg(line, n):
    avg = [0,0,0]
    for i in range(1, n+1):
        avg[i%3-1] += int(float(line[i])/(n/3))
    return avg

def start():
    for _ in range(14):
        line = new()
    return line, dt.now(), len(line)-2
    
line, i, n = start()
while True:
    d = time(i)
    if d >= float(line[0]):
        print(avg(line, n))
        line = new()
        if line[0] == '-1':
            break
