# The drawing below gives an idea
#  of how to cut a given "true"
#  rectangle into squares ("true"
# rectangle meaning that the two
# dimensions are different).
#
#
# Can you translate this drawing
# into an algorithm?
#
# You will be given two dimensions
#
# a positive integer length (parameter named lng)
# a positive integer width (parameter named wdth)
# You will return an array or a string
# (depending on the language; Shell
#  bash and Fortran return a string)
# with the size of each of the squares.


def sqInRect(length, width):
    if length == width:
        return None
    squares = []
    while length != width:
        small = min(length, width)
        big = max(length, width)
        squares.append(small)
        length = small
        width = big - small
    squares.append(small)
    return squares


print(sqInRect(5, 5), None)
print(sqInRect(5, 3), [3, 2, 1, 1])
