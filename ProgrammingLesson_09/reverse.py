

output = ""
myList = ["Hi", "Hey", "Hola", "Hello", "Sup"]

print("In order ..... ")

for i in myList:

    output += i + " "

print(output)
    
print("In Reverse ......")

for i in range(len(myList),0,-1):
    print(myList[i-1])
    
    
