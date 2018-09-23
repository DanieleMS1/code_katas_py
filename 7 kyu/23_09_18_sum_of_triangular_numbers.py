# Your task is to return the sum of
# Triangular Numbers up-to-and-including
#  the nth Triangular Number.
#
# Triangular Number: "any of the
# series of numbers (1, 3, 6, 10, 15, etc.)
# obtained by continued summation of
# the natural numbers 1, 2, 3, 4, 5, etc."
#
# [01]
# 02 [03]
# 04 05 [06]
# 07 08 09 [10]
# 11 12 13 14 [15]
# 16 17 18 19 20 [21]
# e.g. If 4 is given: 1 + 3 + 6 + 10 = 20.
#
# Triangular Numbers cannot be negative so
# return 0 if a negative number is given.


def sum_triangular_numbers(n):
    if n < 1:
        return 0
    return sum(int(i * (i + 1) / 2) for i in range(n + 1))

# ho usato la formula per la somma dei primi n interi -> gauss

# si poteva fare in una linea cosi


def sum_triangular_numbers(n):
    return n * (n + 1) * (n + 2) / 6 if n > 0 else 0

# la formula sopra da come risultato la somma dei primi n numeri triangolari


print(sum_triangular_numbers(6), 56)
print(sum_triangular_numbers(34), 7140)
print(sum_triangular_numbers(-291), 0)
print(sum_triangular_numbers(943), 140205240)
print(sum_triangular_numbers(-971), 0)
print(sum_triangular_numbers(0), 0)
