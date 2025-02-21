# Part 1: Using Functions
# Objective:
# Create a modular calculator that can perform basic arithmetic operations. Write a separate function for each operation: addition,
# subtraction, multiplication, and division.
# 
# Instructions:
# 
# Write functions for the following operations:


addition = lambda num1, num2: num1 + num2
subtraction = lambda num1, num2: num1 - num2
multiplication = lambda num1, num2: num1 * num2
division = lambda num1, num2: "Error: Cannot divide by zero" if num2 == 0 else num1 / num2


def calculator():
    while True:
        selection = input("what do you wanna do pick +, -, * or / q to quit")
        
        if selection == "q":
            print ("goodbyeeeee")
            break
        
        if selection not in ("+","-","*","/"):
            print("yo this aint a valid operator u can be using")
            continue

        num1 = int(input("what is yor first number"))
        num2 = int(input("what is yor second number"))

        if selection == ("+"):
            addition(num1, num2)

calculator()

# Create a main calculator() function that:
# Prompts the user to select an operation (choose from +, -, *, /).
# Prompts the user to input two numbers.
# Calls the corresponding function to perform the operation.
# Prints the result.