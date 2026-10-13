
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

print("""
Welcome to the binomial expansion calculator. Please read below for information on how to use the calculator.

The calculator is designed to give approximations to irrational numbers to a degree of accuracy that you choose.

Enter a fractional power in the form x/y where x is the numerator and y is the denominator between -1 and 1, enter the amount of terms you'd like involved in your approximated expansion
(The more terms, the more accurate your approximation will be), and enter a non-zero positive base.

There are always at least two terms, 1 and nx.
The maximum number of terms that you can select is 160.

Powers that are recurring numbers such as 1/3 will always be truncated to 16 decimal places by default.

The estimated error is the value of the next 10 terms of the expansion.
The estimated error may be in scientific notation form, xe-y. The e is a constant, 10. e-y means 10^-y, and you multiply this value by x, so xe-y means x multiplied by 10^-y.

""")

base = None
n = None
accuracy = None

while base == None:

    try:

        base = float(Fraction(input("What is the base:")))

    except (ValueError, ZeroDivisionError):

        print("Please enter an integer, decimal or fraction as the base.")

while n == None:

    try:
        n = float(Fraction(input("What is the power:")))

    except (ValueError, ZeroDivisionError):

        print("Please enter a decimal or fraction as the power")

while accuracy == None:

    try:
        accuracy = int(input("How many terms would you like (minimum:2):"))

    except (ValueError , ZeroDivisionError):

        print("Please enter an integer as the number of terms you would like")

def binomialexpansion(base, n):

    if n >= 1 or n <= -1:
        return "The power must be a fraction between -1 and 1"

    if base <= 0:
        return "The base must be a positive value"

    if accuracy < 2:
        return "The minimum number of terms is 2"

    if accuracy > 160:
        return "The maximum number of terms is 160"

    count = 0

    while base > 2:

        base /= 4

        count += 1

    multiplier_power = n * count

    multiplier = 4 ** multiplier_power

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

    series_for_error = series

    for i in range(accuracy, accuracy + 10):

        series_for_error += (term * (x ** iterated_power))

        iterated_number -= 1
        iterated_factorial += 1
        iterated_power += 1

        numerator *= (n + iterated_number)
        denominator = factorial(iterated_factorial)

        term = numerator / denominator

    series *= multiplier

    series_for_error *= multiplier

    estimated_error = abs(series_for_error - series)

    print(f"The approximated value for {base} ^ {n} is:",str(series))

    print(f"The estimated error for your value is {estimated_error}")

binomialexpansion(base, n)

#Goal: to create a system for accuracy by using python placeholder values as reference

#The current expansion loses convergence speed as base tends to 0

