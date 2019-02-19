# PythonPractice
Python practice exercises for Machine Learning first exam.

## Equal Letters (Exercise 1)

### Instructions:
A string may contain between three and nine letters. All letters should be equal except one. Write a Python program that receives such string from the keyboard, and checks the two conditions. If at least one of the two conditions is invalid the program prints `INVALID INPUT`, if both conditions are met the program prints the index of the letter that is different from others. 

#### Example:

|string|output|
|------|------|
|ab|`INVALID INPUT (incorrect length)`|
|abb|`INDEX 0`|
|abaa|`INDEX 1`|
|aaaaa|`INVALID INPUT (incorrect content)`|
|bbaab|`INVALID INPUT (incorrect content)`|

## Mean and Standard Deviation (Exercise 2)

### Instructions:
Write a program that receives between three and nine numbers from the keyboard, one by one in a loop. After all numbers are entered the program reports their mean and standard deviation.

## Factorials (Exercise 3)

### Instructions:
The operator ! stands for the factorials, defined as: 0! = 1 and n! = n*(n-1)!

#### Factorial Examples:
- 0! = 1
- 1! = 1
- 2! = 2 * 1 = 2
- 3! = 3 * 2 * 1 = 6
- 4! = 4 * 3 * 2 * 1 = 24

Write a Python program that defines a function for caculating factorials. Then the program asks a user to input an integer 0 to 20 and print out the factorial of such number. The program should check that the input is an integer from interval [0,20], and if not the program should write `INVALID INPUT`.

The function definitions should start as:

```def factorial(n):```

## Random Number Guess (Exercise 4)

### Instructions:
Write a program that generates a random number in the range of 1 through 100 and asks the user to guess what the number is. If the user's guess is higher than the random number, the program should display `Too high, try again.` If the user's guess is lower than the random number, the program should display `Too low, try again.` If the user guesses the number, the application should congratulate the user, report how many attempts the user made and ask user if he/she wants to play again. If the user answers `n` (no) the program exists and if the user answers `y` (yes) a new random number is generated so the game can start over.

## Dice Frequency
### Instruction:
In a program, write a function named `roll` that accepts an integer argument `number_of_throws` . The function should generate and return a sorted list of `number_of_throws` random numbers between 1 and 6. The program should check that the user enters a positive integer that is sent to the function and then prnt the returned list as a table of frequencies with columns `numbers` and `frequencies`.

#### Example:
##### Input:
|`number_of_throws`|20|
|----------------|--|

##### Output:
```
| n |frequencies|
|---|-----------|
| 1 |     3     |
| 2 |     4     |
| 3 |     4     |
| 4 |     2     |
| 5 |     3     |
| 6 |     4     |
```
## Naive Bayes (Exercise 6)
### Instructions
Given de following data:

|Exam 1|Study [h/day]|Pass Exam 2|
|------|-------------|-----------|
|A|2.0|Yes|
|B|1.0|No|
|A|1.0|No|
|C|3.0|Yes|
|B|2.0|Yes|
|C|2.0|No|

We want to use Naive Bayes technique to predict if the student will pass the second exam, given students grade on the first exam and number of hours per day the student studies the material.

Write a python program that receives grade A, B, or C and number of hours 1, 2 or 3 from the user and then predicts if the student with such grade and hours will pass the exam 2.
