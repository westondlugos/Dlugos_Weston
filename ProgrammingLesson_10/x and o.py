import random
XandO = []

for i in range(0,4):
    XandO.append([])
    for j in range(0,4):
        switch = random.randint(0,1)
        if switch == 1:
            XandO.append("X")
        else:
            XandO.append("O")

for values in XandO:
    output = ""
    for value in values:
        output = output + value
    print(output)
    
