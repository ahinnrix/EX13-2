# Amanda Hinnerichs
# April 14, 2024
# EX13-2
# This program asks the user for a mathematical expression, splits the string into
# components, performs the calculation, and returns the result, repeating until the user decides to exit.

#functions+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def calculate_expression(expression):              #Ask for an expression from the user
    num1, op, num2 = expression.split()
    num1 = float(num1)
    num2 = float(num2)

    if op == '+':                        #if statement to perform calculations
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error"
        result = num1 / num2
    elif op == '^':
        result = num1 ** num2
    elif op == '%':
        if num2 == 0:
            return "Error"
        result = num1 % num2
    else:
        return "Error: Invalid operation. Please enter a valid operator (+, -, *, /, ^, %)."

    return f"Your answer is {num1} {op} {num2} = {result}"

def user():              #while loop to continually ask for user input until user decides to quit
    while True:
        user_input = input("Please enter a mathematical expression or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        print(calculate_expression(user_input))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#main++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
user()