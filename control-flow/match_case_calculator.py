# Prompt user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt user for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Use match-case to handle the operation
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation selected.")

