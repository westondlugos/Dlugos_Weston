
number = int(input("Enter a number:"))
digits = 0
num = number
avg = 0

while num > 0:
    digits = digits + 1
    avg = (avg + (num % 10))
    num = int(num / 10)
    

print("The average of the digits of ",number,"is",avg / digits)

    
    
