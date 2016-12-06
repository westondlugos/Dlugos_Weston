import random
print("Numbers....")
numbers = []
for i in range(0,10):
    num = random.randint(1,100)
    numbers.append(num)
    
print(numbers)

print("")

print("The average of the above numbers is...")


def average(numbers):
    avg = 0
    digits = 0
    for i in range(0,10):
        digits = digits + 1
        avg = avg + numbers[i]
    print(avg/digits)

average(numbers)
         




