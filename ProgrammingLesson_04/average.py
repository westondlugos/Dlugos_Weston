def average(num1,num2,num3):
    return((num1 + num2 + num3)/3)

def printAverage(avg):
    print("The average of:""{:10.5f}{:10.5f}{:10.5f}{:^4}{:10.5f}".format(num1,num2,num3,"is",avg))


num1 = float(input("What the first number?"))
num2 = float(input("What the second number?"))
num3 = float(input("What the third number?"))

printAverage(average(num1,num2,num3))

