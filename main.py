from fractions import Fraction


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
    base = input("What is the base:")
    while not isinstance(base, int):
        if base.isdigit():
            base = int(base)
        else:
            print("Please enter an integer")
            base = input("What is the base:")

    n = input("What is the exponent:")
    while not isinstance(n, int):
        if n.isdigit():
            n = int(Fraction((n)))
        else:
            print("Please enter an integer")
            n = input("What is the exponent:")

    accuracy = input("How many terms would you like (minimum:2):")
    while not isinstance(accuracy, int):
        if accuracy.isdigit():
            accuracy = int(accuracy)
        else:
            print("Please enter an integer")
            accuracy = input("How many terms would you like (minimum:2):")

    if n >= 1 and n <= -1:
        return "The power must be a fraction between 0 and 1"

    if base < 0:
        return "The base must be a positve, non-zero integer"

    x = base - 1

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
