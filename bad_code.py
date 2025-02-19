class Calculator:
    def __init__(self):
        # Runs the user input menu and displays the calculation result
        operation = {
            "1": ("+", add),
            "2": ("-", subtract),
            "3": ("*", multiply),
            "4": ("/", divide)
        }

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

            elif choice in operation:
                num1, num2 = get_numbers()
                character, function = operation[choice]
                result = function(num1, num2)

                if result is not None:
                    print(f"\n{num1} {character} {num2} = {result}")

            else:
                print("Invalid input, try again.")
        """
        The version of the calculator that doesn't follow recommended programming practices.
        """

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    # This method
    # demonstrates the easiest
    # possible implementation of
    # multiplicat -
    # ion
    def multiply(x, y):
        total = 0
        for i in range(x):
            total += y
        return total

    def divide(x, y):
        if y == 0:
            print("\nCannot divide by zero")
            return None
        return x / y

