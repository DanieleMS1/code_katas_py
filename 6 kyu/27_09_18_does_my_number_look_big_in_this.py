# A Narcissistic Number is a number
# which is the sum of its own digits,
# each raised to the power of the number of digits.
# Your code must return true or false depending
# upon whether the given number is a Narcissistic number.
#
#  1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#
# Error checking for text strings or other
# invalid inputs is not required, only valid
# integers will be passed into the function.


def narcissistic(value):
    digits = [int(d) for d in str(value)]
    power = len(digits)
    return sum(x**power for x in digits) == value

#possiamo comprimerlo

def narcissistic(value):

    return sum(x**len(str(value)) for x in [int(d) for d in str(value)]) == value





print(narcissistic(7), True)
print(narcissistic(371), True)
print(narcissistic(122), False)
print(narcissistic(4887), False)
