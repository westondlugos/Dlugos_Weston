def calcAverage():
    global num1, num2, num3, avg
    num1 = float(input("What is the first number?"))
    num2 = float(input("What is the second number?"))
    num3 = float(input("What is the third number?"))
    avg = (num1 + num2 + num3)/3

def printAvg():
    print("The average of ""{:10.5f}{:10.5f}{:10.5f}{:^4}{:10.5f}".format(num1 , num2 , num3 ,"is", avg))

calcAverage()
printAvg()

