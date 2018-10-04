# Complete the square sum method so
# that it squares each number passed
# into it and then sums the results
# together.
#
# For example: squareSum([1, 2, 2])
# should return 9 because
# 1^2 + 2^2 + 2^2 = 9.

def square_sum(numbers):
    return sum(x**2 for x in numbers)


print(square_sum([1,2]), 5)
print(square_sum([0, 3, 4, 5]), 50)
