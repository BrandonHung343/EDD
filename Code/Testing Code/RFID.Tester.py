# Use this link to install the program and the library
# http://behindthesciences.com/electronics/raspberry-pi-rfid-tag-reader/
import time
import serial
idNums = []
count = 0

PortRF = serial.Serial('/dev/ttyS0',9600)
while True:
    ID = ""
    read_byte = PortRF.read()
    if read_byte=="\x02":
        for Counter in range(12):
            read_byte=PortRF.read()
            ID = ID + str(read_byte)
        print (ID)
    idNums [count] = ID
    count = count + 1
    if count == 6:
        break
    time.sleep(5)

print (idNums)
