
import random
numsList = []

for i in range(0,4):
    numsList.append([])
    for j in range(0,4):
        numsList[i].append(random.randint(1,100))

output = ""

for nums in numsList:
    output += "\n"
    for num in nums:
        output += str(num) + "\t"
print(output)
div = int(input("Please enter a number:"))




count = 0

for nums in numsList:
    for num in nums:
        if num % div == 0:
            count += 1



print("There are", count, "numbers divisible by", div, "in the list")
    
