

def idcardFormat(idCard,idCard2):
    print("{:2}{:>12}{:>19}{:>2}".format("*",idCard,idCard2,"*"))





idCard = input("Please enter your first name:")
idCard2 = input("Please enter your last name:")
idCard3 = input("Enter your title:")
idCard4 = input("What school do you go to:")
idCard5 = input("What school year is it:")
idCard6 = input("What subject are you?")


print("***********************************")
idcardFormat(idCard4,idCard5);
idcardFormat(idCard,idCard2);
idcardFormat(idCard3,idCard6);
print("***********************************")
