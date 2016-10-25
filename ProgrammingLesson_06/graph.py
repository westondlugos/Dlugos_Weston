size = int(input("What is the size of the table?"))
slope = int(input("What is the slope?"))
intercept = int(input("What is the y intercept?"))

for i in range(0,size+1):
    print(i,(i * slope)+ intercept)
