'''
    Returns the factorial of the given number.
    It takes the number multiplies it and does number minus 1.
'''
def factorial(number):
    result = 1

    #While the number is not 0 keep multiplying it to the result number and input number minus 1 each iteration.
    while number != 0:
        result = result*number
        number = number-1
    
    return result

'''
    Main function where the input is validated so it is not bigger than 20 or less than 0.
    Prints the number returned by the factorial function.
'''
if __name__ == "__main__":

    user_input = int(input("Enter a number from 0 to 20:\n"))
    
    #If the input is correct then print the factorial of the input number.
    if user_input > 20 or user_input < 0:
        print("INVALID INPUT")
    else:
        print("Factorial: " + str(factorial(int(user_input))))
