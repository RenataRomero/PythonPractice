def exercise_frequency_table():
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

    print(grades_exercise_table)

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
        "Total":1
    }

    print(hours_exercise_table)

def naive_bayes(grade, hours):
    pass


def main():
    grade = input("Enter the grade:\n")
    hours = input("Enter the ammount of hours:\n")
    exercise_frequency_table()

main()