# Given an integral number,
# determine if it's a square number


def is_square(n):
    return(n**(1.0/2) % 1 == 0 if n >= 0 else False)


print(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
print(is_square( 0), True, "0 is a square number")
print(is_square( 3), False, "3 is not a square number")
print(is_square( 4), True, "4 is a square number")
print(is_square(25), True, "25 is a square number")
print(is_square(26), False, "26 is not a square number")
