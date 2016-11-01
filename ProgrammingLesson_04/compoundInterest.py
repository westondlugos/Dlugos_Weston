

    



Principal = float(input("Enter the principal here:"))


rate = float(input("enter rate of interest:"))

num = float(input("enter the number of times per year that the interest is compounded:"))

time = float(input("Enter the amount of years:"))


def compoundInterest():
    loanAmount = (Principal * (1 + (rate/num))**(num * time))/(time * 12 )
    output = "{:.2f}".format(loanAmount)
    return output

print("$",compoundInterest())

