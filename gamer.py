import time
import letsplay
prompt = "Would you like to play a game?"
prompt += "\nPlease enter either yes or no\n"
prompt2 = "Would you like to play again?"
prompt2 += "\nPlease enter either yes or no\n"

def check_for_yes_or_no(user_check_to_play):
    if user_check_to_play.lower() not in {'yes','no','y','n'}:
        return True
    else:
        return False
def check_for_int(user_input):
        if type(user_input) != int:
                return True               
        
def noPlay(user_check_to_play):
    if user_check_to_play.lower() in {'no','n'}:
        return True

def instructions(weWantInstructions):
        if weWantInstructions:
                time.sleep(1)
                print("Awesome! ", end="", flush=True)
                time.sleep(0.7)
                print("Let's play", end="", flush=True)
                time.sleep(0.5)
                print(".", end="", flush=True)
                time.sleep(0.5)
                print(".", end="", flush=True)
                time.sleep(0.5)
                print(".", flush=True)
                time.sleep(1.5)
                print("Please pick a number between 1 and 100", flush=True)
                time.sleep(2.5)
                print("You will have 5 chances to pick the correct answer", flush=True)
                time.sleep(2.5)
                print("We will tell you if your guess is close to the number, or not!", flush=True)
                time.sleep(3)
        else:
                return

def winner(users_guess,random_number):
    if users_guess == random_number:
        return True

def hc(users_guess,random_number):
    if users_guess > random_number:
        return "Oooo, you need to guess lower!\n"
    elif users_guess < random_number:
        return "Ooo, you need to guess higher!\n"

def winningOutput(random_number):
    print("Yay!!! You won! It was " + str(random_number) + "!!" )    

def losingOutput(random_number):
    print("Oh, so sorry you didn't guess it :( The number was: " + str(random_number) )

def hearInstructions():
        user_instructions = input("Do you want to hear the instructions?\n")
        while check_for_yes_or_no(user_instructions):
                user_instructions = input("Hey! Please enter either yes or no!\n")
        if user_instructions.lower() in {'yes','y'}:
                display_instructions = True
        else:
                display_instructions = False
        return instructions(display_instructions)   