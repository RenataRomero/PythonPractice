def factorial(number):
    result = 1
    while number != 0:
        result = result*number
        number = number-1
    
    return result

def main():

    user_input = input("Enter a number from 0 to 20:\n")
    if int(user_input) > 20 or int(user_input) < 0:
        print("INVALID INPUT")
    else:
        print("Factorial: " + str(factorial(int(user_input))))

main()