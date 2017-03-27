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
PortRF = serial.Serial('/dev/ttyAMA0',9600)

shelfItems = []
xList = []
yList = []
ID= ""

class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
# create class for our Raspberry Pi GUI

def __init__(self):
# access variables inside of the UI's file
 super(self.__class__, self).__init__()
 self.setupUi(self) 
# gets defined in the UI file


def main():
    #app = QApplication(sys.argv)
    #new app instance
    #form = MainWindow()
    #form.show()
    #sys.exit(app.exec_())
    #prevent app from self-closing
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
        scan() 
        screwActuator.setPos(getXPos(positions, ID), getYPos(positions, ID))


def getXPos(someList, idNum):
    for i in range (len(inventoryList)):
        if idNum == shelfItems[i]:
            x = i
    xPos = someList[x]
    return xPos

def getYPos(someList, idNum):
    for i in range (len(inventoryList)):
        if idNum == shelfItems[i]:
            y = i
    yPos = someList[y]
    return yPos

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
                    ID = str(shelfItems[i])
                    break
                else:
                    ID = str(0)
            if ID != '0':
                return ID
                break
            
def setPos(xPos, yPos):
    
    
    

