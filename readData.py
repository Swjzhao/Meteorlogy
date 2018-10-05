#!/usr/bin/python
import serial
import syslog
import time

#The following line is for serial over GPIO
port = '/dev/ttyACM0'


ard = serial.Serial(port,9600,timeout=5)
i = 0

f = open('data.csv', 'w')
f2 = open('dataAfter.csv', 'w')

while (i < 1050):
    # Serial read section
    msg = ard.readline()
    if(i > 50):
        print (msg)
        f.write(msg)
    i = i + 1
else:
    print ("Exiting")
    f.close()
exit()
