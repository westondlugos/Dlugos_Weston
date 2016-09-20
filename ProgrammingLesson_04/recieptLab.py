




def recieptFormat(item,price):
    print("{:1}{:>16}{:>9}{:>7.2f}".format("*",item,"........",price))

def subtotalFormat(subtotal):
    print("{:1}{:>16}{:>9}{:>7.2f}".format("*","subtotal","........",subtotal))

def taxFormat(tax):
    print("{:1}{:>16}{:>9}{:>7.2f}".format("*","tax","........",tax))

def totalFormat(total):
    print("{:1}{:>16}{:>9}{:>7.2f}".format("*","total","........",total))

item = input("Please enter item 1:")

price = float(input("Plese enter the price of the:"))

item2 = input("Please enter item 2:")

price2 = float(input("Please enter the price:"))

item3 = input("Please enter item 3:")

price3 = float(input("Please enter the price of the:"))

subtotal = price + price2 + price3
tax = subtotal * 0.07
total = tax + subtotal



print("<<<<<<<<<<<<<<<__reciept__>>>>>>>>>>>>>>>")
print("")
print("")
recieptFormat(item,price);
recieptFormat(item2,price2);
recieptFormat(item3,price3);
print("")
print("")
subtotalFormat(subtotal);
taxFormat(tax);
totalFormat(total);
print("__________________________________________")
print("          *Thank You For Support*")
