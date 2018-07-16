numberArray = []

def loadArray():

    for loopCounter in range(101):
        numberArray.append(loopCounter)

def printArray():

    for item in numberArray:
        print("This is the item: ", item)


loadArray()
printArray()