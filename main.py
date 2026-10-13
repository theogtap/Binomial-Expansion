
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

Enter a fractional power between -1 and 1, enter the amount of terms you'd like involved in your approximated expansion
(The more terms, the more accurate your approximation will be), and enter a non-zero positive base.

Powers that are recurring numbers such as 1/3 will always be approximated to 15 decimals places by default.

There are always at least two terms, 1 and nx.
The maximum number of terms that you can select is 169

You may receive values for your maximum error in scientific notation. For example, 5e-16. e-16 means 10^-16, and you multiply that by the number in front. In this case, 5. So 5e-16 = 5 x 10^-16.

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

    series *= multiplier

    print(f"The approximated value for {base} ^ {Fraction(n)} is:",str(series))

binomialexpansion(base, n)

#Goal: to make accuracy measurable by calculating error and creating a system for accuracy

#The current expansion loses convergence speed as base tends to 0

