
number = int(input("Enter a number:"))
s = 0
num = number

while num > 0:
    s = s + (num % 10)
    num = int(num / 10)
    
print("The sum of the digits of" , number, "is ",s)
