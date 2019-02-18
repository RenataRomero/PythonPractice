def naive_bayes(grade, hours):
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

    dividend_no = (grades_exercise_table["No_Total"])*(grades_exercise_table[grade + "_No"]) * (hours_exercise_table[str(hours) + "_No"])
    dividend_yes = (grades_exercise_table["Yes_Total"])*(grades_exercise_table[grade + "_Yes"]) * (hours_exercise_table[str(hours) + "_Yes"])
    divisor = (grades_exercise_table[grade + "_Total"])*(hours_exercise_table[str(hours) + "_Total"])

    yes_prob = dividend_yes/divisor
    no_prob = dividend_no/divisor
    
    if yes_prob > no_prob:
        print("You will pass!!")
    else:
        print("You will not pass /:")

def main():
    grade = input("Enter the grade:\n")
    hours = float(input("Enter the ammount of hours:\n"))
    naive_bayes(grade, hours)

main()