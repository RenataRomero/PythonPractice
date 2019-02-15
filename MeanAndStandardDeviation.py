import math

def summation(numbers):
    summation = 0.0
    for i in numbers:
        summation += i
    return summation

def standard_deviation(mean, numbers, iterations):
    square_median_distance = []

    for i in numbers:
        result = float(i) - mean
        if result < 1:
            result = result*-1
        
        square_result = result**2
        square_median_distance.append(square_result)

    s_m_d_summation = summation(square_median_distance)/iterations
    standard_deviation = math.sqrt(s_m_d_summation)

    return standard_deviation

def mean(summation, iterations):
    return summation/iterations

def main():
    number = 0
    numbers = []
    summation = int(number)
    iterations = 0
    print("Enter numbers 1 by 1 and use * to stop:")
    while number != "*":
        number = input()
        if number != "*":
            summation += int(number)
            numbers.append(int(number))
            iterations += 1

    mean_number = mean(summation, iterations)
    print("Mean: " + str(mean_number))
    print("Standard Deviation: " + str(standard_deviation(mean_number, numbers, iterations)))

main()