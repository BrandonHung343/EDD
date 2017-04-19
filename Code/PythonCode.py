#from PyQt5.QtWidgets import *
# This gets the Qt stuff
#import mainwindow_auto
# This is our window from QtCreator
import time
import sys
import time
import serial
import RPi.GPIO as GPIO
from Stepper.Tester import *
#install these programs on your RPi when you get the chance

GPIO.setmode(GPIO.BCM)
PortRF = serial.Serial('/dev/ttyS0',9600)

shelfItems = []
xList = []
yList = []
ID= ""

def main():
    stepper1 = Stepper(4, 17, 23, 24, 18)
    stepper2 = Stepper()
    #inventoryFile = open('C:\\Users\\dbh101p4u31\\Downloads\\Crackle.txt')
    inventoryList = inventoryFile.readlines()
    #reads the storage file for each entry, puts it into list
    for i in range (len(inventoryList)):
        entry = inventoryList [i]
        xList.insert (i, entry[27])
        yList.insert (i, entry[30])
    
        #adds x and y coordinate to positions dictionary, unless key is already there
        shelfItems.insert(i, entry[:25])
        #sets shelfItems list values to the RFID number
    
#working on 3
    while True:
        index = scan() 
        setPos(getXPos(index), getYPos(index))
        


def getXPos(indexValue):
    return xList[indexValue]

def getYPos(indexValue):
    return yList[indexValue]

def pairing():
	#if the button is pressed to change something
	while changing == True:

def scan():
    while True:
        read_byte = PortRF.read()
        if read_byte=="\x02":
            for Counter in range(12):
                read_byte=PortRF.read()
                ID = ID + str(read_byte)
            print ID
            for i in range(len(shelfItems)):
                if ID == shelfItems[i]:
                    return i
                    break
       
def setPos(xPos, yPos): 
    stepperX.forward(10, xPos*512)
    stepperY.forward(10, yPos*512)
    
    
    
    

