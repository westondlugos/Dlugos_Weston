item1 = input("What did you buy?");
price1 =float(input("What was the of price of the "+item1+"?"));
item2 = input("What was the second thing you bought?");
price2 = float(input("What was the price of the "+item2+"?"));
item3 = input("What was the third thing you bought?");
price3 = float(input("What was the price of the "+item3+"?" ));
item4 = input("What was the fourth thing you bought?");
price4 = float(input("What was the price of the "+item4+"?"));
subtotal = price1 + price2 + price3 + price4
tax = subtotal * 0.10
discount = 0

if subtotal >= 2000:
    discount = subtotal * 0.15

total = subtotal + tax - discount




def formatF():
    print("{:10}{:^9}{:10}".format("<<<<<<<<<<","Reciept",">>>>>>>>>>"))
    print("{:<23}{:<4.2f}".format(item1,price1))
    print("{:<23}{:<4.2f}".format(item2,price2))
    print("{:<23}{:<4.2f}".format(item3,price3))
    print("{:<23}{:<4.2f}".format(item4,price4))
    print("{:<23}{:<4.2f}".format("subtotal",subtotal))     
    print("{:<23}{:<4.2f}".format("tax",tax))
    print("{:<23}{:<4.2f}".format("discount",discount)) 
    print("{:<23}{:<4.2f}".format("total",total))
    print("_____________________________")
    print(" Thank you for shopping here")


formatF()
