def calcPerim(length,width):
    return (2 * length)+(2 * width)

def display(num):
    print("Your rectangle is""{:10.5f}{:>12}".format(num,"feet around")) 
    

length = float(input("What is the length of the rectangle?"))
width = float(input("What is the width of the rectangle?"))

display(calcPerim(length,width))

