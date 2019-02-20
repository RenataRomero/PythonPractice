import random

'''
    Returns a random number form 1 to 6.
'''
def generate_random_number():
    return random.randint(1,6)

'''
    Returns a dictionary with the frequencies of each number of the dice.
'''
def roll(number_of_throws):
    dice_dictionary = {}
    dice_dictionary[1] = 0
    dice_dictionary[2] = 0
    dice_dictionary[3] = 0
    dice_dictionary[4] = 0
    dice_dictionary[5] = 0
    dice_dictionary[6] = 0

    #For every roll.
    for n in range(number_of_throws):
        #Check the random number and add 1.
        dice_number = generate_random_number()
        dice_dictionary[dice_number] += 1

    return dice_dictionary

'''
    Formatting for the frequency table.
'''
def build_frequency_table(dictionary):
    print("x | frequency")
    print("-------------")
    for key in dictionary:
        print(str(key) + " | " + str(dictionary[key]))
        
'''
    Main function where the input is validated so it always is positive 
    and prints the frequency table with the build_frequency_table format.
'''
def main():
    #Gets the number of throws.
    number_of_throws = int(input("Enter the number of throws:\n"))

    #Validates the number of throws, if it's not correct, tray again.
    while number_of_throws <= 0:
        print("INVALID INPUT, please enter a positive number and different from 0.")
        number_of_throws = int(input("Enter the number of throws:\n"))
    
    #Prints the frequency table.
    build_frequency_table(roll(number_of_throws))

main()