xList = []
yList = []
shelfItems = []
inventoryFile = open('C:\\Users\\dbh101p4u31\\Downloads\\Crackle.txt')
inventoryList = inventoryFile.readlines()
print (inventoryList)
    #reads the storage file for each entry, puts it into list
for i in range (len(inventoryList)):
    entry = inventoryList [i]
    xList.insert (i, entry[27])
    yList.insert (i, entry[30])
    
        #adds x and y coordinate to positions dictionary, unless key is already there
    shelfItems.insert(i, entry[:25])
        #sets shelfItems list values to the RFID number
def rock():
    print (positions)
    print (shelfItems)
    
#working on 3
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
