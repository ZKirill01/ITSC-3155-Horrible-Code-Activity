from functools import total_ordering


class Calculator:
    """
    The version of the calculator that doesn't follow recommended programming practices.
    """

    starting_value = 0

    # The constructor initializes starting value!
    def __init__(self, starting_value):
        self.starting_value = 0

    """ This method declares a variable.
        Then this method ensures addition is required and stores the sum of addition.
        Then the method returns the sum of addition stored in the variable.
    """
    def add(x, y, flag):
        total = starting_value
        if flag:
            total = x + y
        else:
            print("Addition failed.")
        return total

    """ This method declares a variable.
        Then this method ensures addition is required and stores the difference of variables.
        Then the method returns the difference stored in the variable.
    """
    def subtract(x, y, flag):
        total = starting_value
        if flag:
            total = x + y
        else:
            print("Subtraction failed.")
        return total

    # This method
    # demonstrates the easiest
    # possible implementation of
    # multiplicat -
    # ion
    def multiply(x, y):
        total = starting_value
        for i in range(x):
            total += y
        return total

    """ This method does something. """
    def divide(x, y):
        if y == 0:
            print("\nCannot divide by zero")
            return None
        return x / y

    """Find a number the user wants, flag to make sure they want it."""
    def pick_nums(flag):
        if flag:
            while True:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))
                return num1, num2
        else:
            print("Hey this won't work.")

# Test run of the calculator
calculator = Calculator(99999999)
print("welcome to the calculator")

