# Take an integer n (n >= 0) and
# a digit d (0 <= d <= 9) as an
# integer. Square all numbers k
# (0 <= k <= n) between 0 and n.
# Count the numbers of digits d
# used in the writing of all the
# k**2. Call nb_dig (or nbDig or ...)
# the function taking n and d as
# parameters and returning this count.

def nb_dig(n, d):
    counter = 0
    squares = [str(x**2) for x in range(n+1)]
    for square in squares:
        digits = [c for c in square]
        for digit in digits:
            if digit == str(d):
                counter += 1
    return counter

#fatto vediamo se posso renderlo piu veloce ora è O(n^2)




print(nb_dig(5750, 0), 4700)
print(nb_dig(11011, 2), 9481)
print(nb_dig(12224, 8), 7733)
print(nb_dig(11549, 1), 11905)
