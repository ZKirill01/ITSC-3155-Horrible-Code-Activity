class Calculator:
    """
    The version of the calculator that doesn't follow recommended programming practices.
    """

    starting_value = 0
    operations = {}

    # The constructor initializes starting value!
    def __init__(self, starting_value):
        self.starting_value = 0
        print("welcome to the calculator")
        self.operation = {
        "1": ("+", self.add),
        "2": ("-", self.subtract),
        "3": ("*", self.multiply),
        "4": ("/", self.divide)
    }

    """ This method declares a variable.
        Then this method ensures addition is required and stores the sum of addition.
        Then the method returns the sum of addition stored in the variable.
    """
    def add(self, x, y, flag):
        total = self.starting_value
        if flag:
            total = x + y
        else:
            print("Addition failed.")
        return total

    """ This method declares a variable.
        Then this method ensures addition is required and stores the difference of variables.
        Then the method returns the difference stored in the variable.
    """
    def subtract(self, x, y, flag):
        total = self.starting_value
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
    def multiply(self, x, y, flag):
        if flag:
            total = self.starting_value
            for i in range(int(x)):
                total += y
            return total
        else:
            print("Multiplication IMPOSSIBLE!.")

    """ This method does something. """
    def divide(self, x, y, flag):
        if flag:
            if y == 0:
                print("\nCannot divide by zero")
                return None
            return x / y
        else:
            print("Division IMPOSSIBLE.")

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

while True:
    print("\nSelect operation:")
    print("\n\t1.Add")
    print("\t2.Subtract")
    print("\t3.Multiply")
    print("\t4.Divide")
    print("\t5.Quit")

    choice = input("\nEnter choice(1/2/3/4/5): ")

    if choice == "5":
        print("\nQuitting...")
        break

    elif choice in calculator.operation:
        num1, num2 = calculator.pick_nums()
        character, function = calculator.operation[choice]
        result = function(num1, num2, True)

        if result is not None:
            print(f"\n{num1} {character} {num2} = {result}")
        else:
            print("Invalid input, try again.")


