from computer import Calculator  # Import the Calculator class
from menu import display_menu  # Import the menu display function

def main():
    calculator = Calculator()  # Create an instance of Calculator

    while True:
        display_menu()  # Show the menu
        operator = input("Operator: ")

        if operator.lower() == "q":  # Exit condition
            print("Exiting calculator.")
            break

        num1 = float(input("Enter first number: "))  # Get first number
        num2 = float(input("Enter second number: "))  # Get second number

        result = calculator.calculate(operator, num1, num2)  # Perform calculation
        print(f"Result: {result}")  # Display result

if __name__ == "__main__":
    main()  # Run the program when executed