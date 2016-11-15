number = int(input("Enter a number:"))
num = number
rev = 0

while num > 0 :
    rev = rev * 10

    rev = rev + (num % 10)
    num = int(num / 10)

print("Th reverse of ",number," is ",rev)
