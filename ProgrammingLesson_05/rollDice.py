print("Hi Im Bert and today I will be trying to beat you in a game roll dice")

import random
num = random.randint(1,6)
compNum = random.randint(1,6)

win = num > compNum
tie = num == compNum

print(num)
print(compNum)

print("You rolled a",num)
print("I rolled a",compNum)



if win:
    print("Ah man! You beat me")

if num < compNum:
    print("Hah I beat you!")

if tie:
    print("we tied")

 


