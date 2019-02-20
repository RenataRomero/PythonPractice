import random
'''
    Returns a random number and notifies the user that the random number is generated.
'''
def generate_random_number():
    print("Random number generated!! Try entering a guess.")
    return random.randint(1,100)

'''
    Runs the main program and this is where the guess of the user is evaluated.
'''
if __name__ == "__main__":
    try_again = True
    attempts = 0

    #While the player wants to try again.
    while try_again == True:
        #Generate random number.
        random_number = generate_random_number()
        guess_number = 0

        #While the number the player enters is different from the random number keep asking for a guess.
        while guess_number != random_number:
            guess_number = int(input("Enter a guess: \n"))
            #If the guess is lower then print higher message and adds an attempt.
            if guess_number > random_number:
                attempts += 1
                print("Too high, try again")
            #If the guess is lower then print lower message and adds an attempt.
            elif guess_number < random_number:
                attempts += 1
                print("Too low, try again")

        #Congratulate if the player guess the random number.
        print("Congratulations!! you guessed the number: "+ str(random_number) +"!!\n")
        #Print the number of attempts.
        print("You did", attempts, "attempts!!")
        
        #Asks if player wants to play again.
        answer = input("Do you want to play again? (y/n)\n")
        
        #If the player doesn't want to, leave the game.
        if answer == "n":
            try_again = False
