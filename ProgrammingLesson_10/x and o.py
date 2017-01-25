import random
XandO = []

for i in range(0,4):
    XandO.append([])
    for j in range(0,4):
        switch = random.randint(0,1)
        if switch == 1:
            XandO[i].append("X")
        else:
            XandO[i].append("O")
output =""
for values in XandO:
    output += "\n"
    for value in values:
        output += value + "\t"

print(output)

print(XandO)
    
