# Given an array of integers (x),
# return the result of multiplying
# the values together in order. Example:
#
# [1, 2, 3] --> 6
# For the beginner, try to use the
# reduce method - it comes in very
# handy quite a lot so is a good one
# to know.
#
# Array will not be empty.

#primo metodo banale


def grow(arr):
    mult = 1
    for i in arr:
        mult *= i
    return mult
#ok ho capito come funziona reduce
from functools import reduce

def grow(arr):
    multiply = lambda x, y: x*y
    return reduce(multiply, arr)

# facciamola in una sola linea

def grow(arr):
    return reduce(lambda x, y: x*y, arr)

print(grow([1, 2, 3]), 6)
print(grow([4, 1, 1, 1, 4]), 16)
print(grow([2, 2, 2, 2, 2, 2]), 64)
