

def calcPerim():
    perimeter = (2 * length)+(2 * width)
    print("Your rectangle is ""{:5.5f}{:^11}".format(perimeter,"ft around"))
def setVariables():
    global length, width, perimeter
    length = float(input("What is the length of the rectangle?"))
    width = float(input("What is the width of the rectangle?"))

setVariables()
calcPerim()









