def calcSurf():
    global side, sa
    side = float(input("What is the length of a side of your cube?"))
    sa = (side**2) * 6

def printSa():
    print("The surface area of a cube whose sides are""{:10.5f}{:^14}{:10.5f}".format(side, "in length is",sa))


calcSurf()
printSa()
