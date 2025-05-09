#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

"""
This is the main function that handles the command-line interface for the
calculator program. It accepts three arguments: two integers and an
operator, performs the corresponding arithmetic operation, and prints the
result.

The function performs the following tasks:
- Checks if the number of arguments is exactly 3.
- Converts the arguments into integers.
- Maps the operator to the appropriate function
(addition, subtraction, etc.).
- Handles invalid operators and prints a message
if the operator is unknown.

Usage:
    python3 100-my_calculator.py <a> <operator> <b>

Arguments:
    a (int): The first number for the arithmetic operation.
    operator (str): The operator for the operation ('+', '-', '*', '/').
    b (int): The second number for the arithmetic operation.

Returns:
    None: The function prints the result of the operation or an
    error message.
"""
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
operator = sys.argv[2]
operation = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

if __name__ == "__main__":
    if operator in operation:
        result = operation[operator](a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
