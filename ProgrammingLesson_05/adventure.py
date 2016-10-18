

def adventure():
    choice1 = input("In your story would you like to be the hero or the villain?")
    if choice1 == "hero" or choice1 == "villain":
        if choice1 == "villain":
            print("Your story begins when you were just a baby.")
            print("when you were only 2 years old your parents were killed.")
            print("You decided that all people were evil and you grew to hate all people and you wanted them all dead.")
            choiceV1 = input("When you were older you came across to villages there names were utopia and tumpton.\n Would you like to destroy utopia or tumpton?")
            if choiceV1 == "tumpton":
                print("Instead of killing everyone you decide to enslave them.")
                print("One night they slip poison into your food and you die.")
                playagain5 = input("Would you like to play again?")
                if playagain5 == "yes":
                    adventure()
            if choiceV1 == "utopia":
                print("You kill everyone in the village except for one ten year old boy.")
                print("You search for him everywhere but nver find him.")
                print("eventually you forget about him until oneday he comes back to find you.")
                print("After a huge battle he beats you.")
                playagain4 = input("Would you like to play again?")
                if playagain4 == "yes":
                    adventure()
        if choice1 == "hero":
            print("Your story begins in the town of Utopia")
            print("When you were 10 years old the villian Gart attacked Utopia and killed your family")

            choiceH1 = input("When you escaped you ran away from the village, later that week you came to a fork in the path.\n Would you like to go to left or right side of the fork?")
            if choiceH1 == "right":
                print("There was a bear at the end of the path and you got eaten")
                playagain = input("Would you like to try again?")
                if playagain == "yes":
                    adventure()
            else:
                print("You walked to the end of the path")
                choiceH2 = input("At the end of the path there was a forrest and a cave.\n Would you like to go into the cave or the forrest?")
            if choiceH2 == "forrest":
                print("While walking through the forrest you get lost.  You never find your way out of the forrest and sadly you die there.")
                playagain2 = input("Would you like to play again")
                if playagain2 == "yes":
                    adventure()
            if choiceH2 == "cave":
                choiceH3 = input("While walking you find a sword.  You walk a little bit further and then see a giant spider.\n Do you want to fight or run?")
            
            if choiceH3 == "fight" :
                print("After defeating the giant spider you find a temple.  At this temple you train for many years then you find the villain that destroyed your town and avenge your family by killing him.")
            if choiceH3 == "run":
                print("While running you trip and fall over a rock then the spider eats you.")
                playagain3 = input("Would you like to play again?")
                if playagain3 == "yes":
                    adventure()

       
        
    else:
        print("Plese pick hero or villain")
        adventure()
        
        
        

adventure()
