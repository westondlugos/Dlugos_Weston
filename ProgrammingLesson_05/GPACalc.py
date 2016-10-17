math = input("What is your math grade?");
english = input("What is your english grade?");
PE = input("What is your PE grade?");
biology = input("What is your biology grade?");
compsci = input("What is your computer science grade?");
videofilm = input("What is your video film grade?");
spanish = input("What is your spanish grade?");



def gcal(grade):
    if grade == "A":
        return 4.0
    elif grade == "B":
        return 3.0
    elif grade == "C":
        return 2.0
    elif grade == "D":
        return 1.0
    else :
        return 0.0

print("Your GPA is: ",(gcal(math)+gcal(english)+gcal(PE)+gcal(biology)+gcal(compsci)+gcal(videofilm)+gcal(spanish))/7)


    
