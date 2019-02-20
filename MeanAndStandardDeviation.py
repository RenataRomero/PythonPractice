import math
'''
    Returns the summation of the numbers in a list.
'''
def summation(numbers):
    summation = 0.0
    for i in numbers:
        summation += i
    return summation

'''
    Returns the standard deviation following the standard deviation formula.
'''
def standard_deviation(mean, numbers, iterations):
    square_median_distance = []

    #For each number the user entered, get the square of the median distance.
    for i in numbers:
        result = float(i) - mean
        if result < 1:
            result = result*-1
        square_result = result**2
        square_median_distance.append(square_result)

    #Once you get all the distances, get the summation and divide it with the number of numbers.
    s_m_d_summation = summation(square_median_distance)/iterations
    #Now get the root square of the las result.
    standard_deviation = math.sqrt(s_m_d_summation)

    #And you get the standard deviation.
    return standard_deviation

'''
    Returns the mean of the numbers entered by the user 
    wih the help of the summation of the numbers and the number of numbers.
'''
def mean(summation, iterations):
    return summation/iterations

'''
    Main function where the list of numbers is created from the inputs of the user and the number of inputs.
    Validates that the user can only enter 3 to 9 inputs.
    Calls the mean and standard_deviations to print the results.
'''
def main():
    number = 0
    numbers = []
    summation = int(number)
    iterations = 0
    print("Enter from 3 to 9 numbers 1 by 1 and use * to stop:")

    #The user needs to enter a * to finish.
    while number != "*":
        number = input()
        if number != "*":
            #Getting the summation of all the number inputs.
            summation += int(number)
            #Filling the numbers list with the inputs.
            numbers.append(int(number))
            #Number of numbers.
            iterations += 1
        else:
            #Validations so the user enters more than 3 numbers but less or equal to 9.
            if iterations < 3:
                print("Not enough numbers, try again with at least 3 numbers.")
                number = 0
                numbers = []
                summation = 0
                iterations = 0
            elif iterations > 9:
                print("You have passed the limit number, try again with less than 9 numbers or 9 numbers.")
                number = 0
                numbers = []
                summation = 0
                iterations = 0
                
    #If everything is correct print mean and standard deviation.
    mean_number = mean(summation, iterations)
    print("Mean: " + str(mean_number))
    print("Standard Deviation: " + str(standard_deviation(mean_number, numbers, iterations)))

main()