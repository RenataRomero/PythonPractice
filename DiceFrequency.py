import random

def generate_random_number():
    return random.randint(1,6)

def roll(number_of_throws):
    dice_dictionary = {}
    dice_dictionary[1] = 0
    dice_dictionary[2] = 0
    dice_dictionary[3] = 0
    dice_dictionary[4] = 0
    dice_dictionary[5] = 0
    dice_dictionary[6] = 0

    for n in range(0,number_of_throws):
        dice_number = generate_random_number()
        dice_dictionary[dice_number] += 1

    return dice_dictionary

def build_frequency_table(dictionary):
    print("x | frequency")
    print("-------------")
    for key in dictionary:
        print(str(key) + " | " + str(dictionary[key]))
        

def main():

    number_of_throws = int(input("Enter the number of throws:\n"))

    while number_of_throws <= 0:
        print("INVALID INPUT, please enter a positive number and different from 0.")
        number_of_throws = int(input("Enter the number of throws:\n"))

    build_frequency_table(roll(number_of_throws))

main()