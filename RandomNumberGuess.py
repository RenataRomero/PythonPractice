import random

def generate_random_number():
    print("Random number generated!! Try entering a guess.")
    return random.randint(1,100)

def main():
    try_again = True
    attempts = 0
    while try_again == True:
        random_number = generate_random_number()
        guess_number = 0
        while guess_number != random_number:
            guess_number = int(input("Enter a guess: \n"))
            if guess_number > random_number:
                attempts += 1
                print("Too high, try again")
            elif guess_number < random_number:
                attempts += 1
                print("Too low, try again")
        
        print("You guessed the number: "+ str(random_number) +"!!\n")
        print("You did", attempts, "attempts!!")
        
        answer = input("Do you want to play again? (y/n)\n")
        
        if answer == "n":
            try_again = False

main()

