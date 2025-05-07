#!/usr/bin/python3
def fizzbuzz():
    """
    Prints numbers from 1 to 100 with substitutions:
    - 'Fizz' for multiples of 3
    - 'Buzz' for multiples of 5
    - 'FizzBuzz' for multiples of both
    Each value is followed by a space, all on the same line.
    """
    output = ""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            output = "FizzBuzz"
        elif i % 3 == 0:
            output = "Fizz"
        elif i % 5 == 0:
            output = "Buzz"
        else:
            output = str(i)
        print("{} ".format(output), end="")
