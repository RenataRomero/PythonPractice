'''
    Prints if the user is passing the second exam or not accourding to the user inputs.
'''
def naive_bayes(grade, hours):
    #Creates relative frequency table of the grades accourding to the instructions data.
    grades_exercise_table = {
        "A_No":1/3,
        "A_Yes":1/3,
        "A_Total":2/6,
        "B_No":1/3,
        "B_Yes":1/3,
        "B_Total":2/6,
        "C_No":1/3,
        "C_Yes":1/3,
        "C_Total":2/6,
        "No_Total":3/6,
        "Yes_Total":3/6,
        "Total":1
    }

    #Creates relative frequency table of the hours accourding to the instructions data.
    hours_exercise_table ={
        "1.0_No":2/3,
        "1.0_Yes":0,
        "1.0_Total":2/6,
        "2.0_No":1/3,
        "2.0_Yes":2/3,
        "2.0_Total":3/6,
        "3.0_No":0,
        "3.0_Yes":1/3,
        "3.0_Total":1/6,
        "No_Total":3/6,
        "Yes_Total":3/6,
        "Total":1
    }

    #Prepares the dividend and divisor depending if it is the probability of passing or not.
    dividend_no = (grades_exercise_table["No_Total"])*(grades_exercise_table[grade + "_No"]) * (hours_exercise_table[str(hours) + "_No"])
    dividend_yes = (grades_exercise_table["Yes_Total"])*(grades_exercise_table[grade + "_Yes"]) * (hours_exercise_table[str(hours) + "_Yes"])
    divisor = (grades_exercise_table[grade + "_Total"])*(hours_exercise_table[str(hours) + "_Total"])

    #Gets each probability.
    yes_prob = dividend_yes/divisor
    no_prob = dividend_no/divisor
    
    #Prints the probability and if the student passed based on the bigger probability.
    if yes_prob > no_prob:
        print("Your passing probability is:", yes_prob)
        print("You will pass!!")
    else:
        print("Your probability of not passing is:", no_prob)
        print("You will not pass :(")
'''
    Main function that gets and validates the user inputs and also calls naive_bayes function.
'''
if __name__ == "__main__":
    #Gets the user inputs.
    grade = input("Enter the grade (A/B/C):\n").upper()

    #Validates de grade input.
    while grade != "A" and grade != "B" and grade != "C":
        print("Incorrect input, please enter one of this grades: A, B or C.")
        grade = input("Enter the grade (A/B/C):\n").upper()
    
    hours = input("Enter the ammount of hours (1/2/3):\n")
    
    #Validates the hour input.
    while hours != "1" and hours != "2" and hours != "3":
        print("Incorrect input, please enter one of this hours: 1, 2 or 3.")
        hours = input("Enter the ammount of hours (1/2/3):\n")
    
    hours = float(hours)

    #Calls the naive_bayes function giving it the user inputs.
    naive_bayes(grade, hours)
