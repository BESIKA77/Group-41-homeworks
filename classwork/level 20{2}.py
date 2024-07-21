def perform_operation(num1, num2, operator):
    """
    Perform arithmetic operation on two numbers based on the given operator.

    Args:
    - num1 (float or int): First operand.
    - num2 (float or int): Second operand.
    - operator (str): Operator to perform the operation. Valid operators are '+', '-', '*', '/'.

    Returns:
    - float or int: Result of the operation.
    - str: Error message if division by zero or invalid operator.

    """
    if operator == '+':  # Addition
        return num1 + num2
    elif operator == '-':  # Subtraction
        return num1 - num2
    elif operator == '*':  # Multiplication
        return num1 * num2
    elif operator == '/':  # Division
        if num2 != 0:  # Check for division by zero
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

# Example usage:
result = perform_operation(5, 3, '+')
print(f"Result: {result}")  # Output: Result: 8

result = perform_operation(10, 2, '/')
print(f"Result: {result}")  # Output: Result: 5.0

result = perform_operation(7, 0, '/')
print(f"Result: {result}")  # Output: Result: Error: Division by zero

result = perform_operation(4, 2, '^')
print(f"Result: {result}")  # Output: Result: Error: Invalid operator