3#!C:\Python\python.exe

import serial
import cgi
import sys
import time
from Query import On, Off

ser = serial.Serial('COM10', 9600)
time.sleep(2)  

previous = None

while True:
    msg = ser.readline()
    current = msg.decode('utf-8').strip()

    if previous != current:
        if "ON" in current:
            print("LED ON!")
            On().execute()
        elif "OFF" in current:
            print("LED OFF!")
            Off().execute()
        else:
            print("Unknown state:", current)

    previous = current
