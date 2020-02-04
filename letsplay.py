import gamer as g
def game():
    import random
    number_of_guesses_left = 5
    random_number = random.randint(1,100)
    #print(random_number)
    loser = True
    while number_of_guesses_left != 0:
        print("You have " + str(number_of_guesses_left) + " guesses left.")
        while True:
            try:
                user_guess = int(input("Guess a number!\n"))
                break
            except ValueError:
                print("Oops! That was not a number! Try again..")       
        if g.winner(user_guess,random_number):
            g.winningOutput(random_number)
            loser = False
            break
        else:
            print(g.hc(user_guess,random_number))
        number_of_guesses_left -=1

    if loser:
        g.losingOutput(random_number)

def playAgain():
    user_check_to_play = input(g.prompt2)
    while g.check_for_yes_or_no(user_check_to_play):
        user_check_to_play = input("Please enter either yes or no\n")
    if g.noPlay(user_check_to_play):
        quit()
    else:
        g.hearInstructions()
    game()
