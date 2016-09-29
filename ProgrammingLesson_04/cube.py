def calcSurf(side):
    return 6 * (side**2)

def surfPrint(sa):
    print("The surface area of this cube with ""{:7.5f}{:^10}{:7.5f}{:7}".format(side,"sides is",sa," in**2"))

side = float(input("What is the length of one side of the cube in inches?"))
sa = 6 * (side**2)

surfPrint(calcSurf(side))
