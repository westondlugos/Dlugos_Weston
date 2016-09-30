r = float(input("What is the radius of the circle?"))

def calcArea():
    area = 3.14 * (r**2)
    return area

print("The area of a circle with the radius of ""{:5.5f}{:^4}{:5.5f}".format(r,"is",calcArea()))
