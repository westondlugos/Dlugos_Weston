def circleArea():
    global radius, area
    radius = float(input("What is the radius of the circle?"))
    area = 3.14 * (radius**2)

def printArea():
    print("The area of the circle with a radius of ""{:10.5f}{:^4}{:10.5f}".format(radius,"is", area))


circleArea()
printArea()
