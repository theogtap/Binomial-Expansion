def factorial(number):
    if not isinstance(number, int):
        return "Please enter an integer as the factorial"

    if number < 0:
        return "Factorial is not defined for negative numbers"

    result = 1

    while number > 1:
        result *= number
        number -= 1

    return result


print("""Welcome to the binomial expansion calculator. 

The calculator is designed to give approximations to irrational numbers to a degree of accuracy that you choose.

Enter a fractional power between zero and one, enter the amount of terms you'd like involved in your approximated expansion 
(The more terms, the more accurate your approximation will be), and enter a non-zero base between -1 and 1.

Powers that are recurring numbers such as 1/3 will always be approximated to 15 decimals places by default.

There are always at least two terms, 1 and nx.
""")

def binomialexpansion():
    base = input("What is the base (non zero and between -1 and 1): ")
    while not isinstance(base, float):
        if base.removeprefix("-").replace(".", "", 1).isdigit():
            base = float(base)
            if base == 0 or base >= 1 or base <= -1:
                print("Please enter a number between -1 and 1 and non zero")
                base = input("What is the base (non zero and between -1 and 1): ")
        else:
            print("Please enter a number")
            base = input("What is the base:")

    n = input("What is the power (between 0 and 1): ")
    while not isinstance(n, float):
        if n.replace(".", "", 1).isdigit():
            n = float(n)
            if n >= 1 or n <= -1:
                print("The power must be a fraction between 0 and 1")
                n = input("What is the power (between 0 and 1): ")
        else:
            print("Please enter a number")
            n = input("What is the power (between 0 and 1): ")

    accuracy = input("How many terms would you like (minimum:2): ")
    while not isinstance(accuracy, int):
        if accuracy.isdigit():
            accuracy = int(accuracy)
            if accuracy < 2:
                print("Please enter a number greater than or equal to 2")
                accuracy = input("How many terms would you like (minimum:2): ")
        else:
            print("Please enter a whole number")
            accuracy = input("How many terms would you like (minimum:2):")

    x = base

    series = 1 + (n * x)

    iterated_number = -1
    iterated_factorial = 2
    iterated_power = 2

    denominator = factorial(iterated_factorial)
    numerator = (n * (n + iterated_number))

    term = numerator / denominator

    for i in range(2, accuracy):
        series += (term * (x ** iterated_power))

        iterated_number -= 1
        iterated_factorial += 1
        iterated_power += 1

        numerator *= (n + iterated_number)
        denominator = factorial(iterated_factorial)

        term = numerator / denominator

    return str(series)


print(binomialexpansion())
