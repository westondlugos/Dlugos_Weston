

username = input("what would you like your username to be?")
password = input("What would you like your password to be?")


def passCheck():
    enterU = input("What is your username?")
    if enterU == username:
        enterP = input("What is your password?")
        if enterP == password:
            print("You are granted access")
        else:
            print("That is not your password.")
            passCheck()
    else:
        print("That is not your username.")
        passCheck()


passCheck()

    

