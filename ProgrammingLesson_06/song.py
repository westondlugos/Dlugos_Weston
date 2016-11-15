

def song():
    song = input("What word do you want in your song?")
    times = int(input("How many times do you want it repeated?"))
    song2 = input("What is the next word you want in your song?")
    times2 = int(input("How many times do you want it repeated?"))
    song3 = input("What is the next word you want in your song?")
    times3 = int(input("How many times do you want it repeated?"))
    song4 = input("What is the next word you want in your song?")
    times4 = int(input("How many times do you want it repeated?"))
    for i in range(0,times):
        song = song + " "
    print(song * times)
    for i in range(0,times2):
        song2 = song2 + " "
    print(song2 * times2)
    for i in range(0,times3):
        song3 = song3 + " "
    print(song3 * times3)
    for i in range(0,times4):
        song4 = song4 + " "
    print(song4 * times4)
    
    


song()





