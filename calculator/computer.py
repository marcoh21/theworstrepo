class Calculator:
    def __init__(self):
        pass  # No attributes needed since we're not storing any data

    def calculate(self, operator, num1, num2):
        # Perform the appropriate calculation based on the operator
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error: Division by zero"  # Prevent division by zero
            return num1 / num2
        else:
            return "Invalid operator" 