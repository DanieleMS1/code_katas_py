# Consider integer numbers from 0 to n - 1
# written down along the circle in such a way
# that the distance between any two
# neighbouring numbers is equal
# (note that 0 and n - 1 are neighbouring, too).
#
# Given n and firstNumber/first_number, find the
# number which is written in the radially
# opposite position to firstNumber.

from math import floor


def circle_of_numbers(n, fst):
    array = [x for x in range(n)]
    return array[floor(fst + n / 2) % n]

# array circolare si fa con % n


print(circle_of_numbers(10, 2), 7)
print(circle_of_numbers(10, 7), 2)
print(circle_of_numbers(4, 1), 3)
print(circle_of_numbers(6, 3), 0)
