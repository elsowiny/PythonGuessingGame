import letsplay
import gamer as g

user_check_to_play = input(g.prompt)
#Check to see if the user puts anything besides yes or no
while g.check_for_yes_or_no(user_check_to_play):
    user_check_to_play = input("Please enter either yes or no\n")
#if they dont want to play quit 
if g.noPlay(user_check_to_play):
    quit()
else:
    g.hearInstructions()
    letsplay.game()
#if they want to play, lets play



playGameAgain = True

while playGameAgain: 
    letsplay.playAgain()




if __name__ == "__main__":
    pass