# The aim of the kata is to decompose n!
# (factorial n) into its prime factors.
# Examples:
# n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
# since 12! is divisible by 2 ten times, by 3 five
# times, by 5 two times and by 7 and 11 only once.
# n = 22; decomp(22) -> "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"
# n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
# Prime numbers should be in increasing order.
# When the exponent of a prime is 1 don't put the exponent.
# Notes
# the function is decomp(n) and should
# return the decomposition of n! into its prime
# factors in increasing order of the primes, as a string.
# factorial can be a very big number (4000! has 12674
# digits, n will go from 300 to 4000).

from math import factorial

def all_prime_factors(n):
    all_factors = []
    i = 2
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n = n // i
            all_factors.append(i)
    if n > 1:
        all_factors.append(n)

    return all_factors


def decomp(n):
    n_fact = factorial(n)
    factors = all_prime_factors(n_fact)
    string_of_factors = ""
    dict_counts = {}
    set_of_factors = sorted(set(factors))
    for fact in set_of_factors:
        dict_counts[fact] = factors.count(fact)

    for key, power in dict_counts.items():
        if power == 1:
            string_of_factors += "{} ".format(key)
        else:
            string_of_factors += "{}^{} ".format(key, power)

    string_of_factors = string_of_factors[:-1]
    string_of_factors = string_of_factors.replace(" ", " * ")
    return string_of_factors


# print(decomp(5) == "2^3 * 3 * 5")
# print(decomp(14) == "2^11 * 3^5 * 5^2 * 7^2 * 11 * 13")
# print(decomp(17) == "2^15 * 3^6 * 5^3 * 7^2 * 11 * 13 * 17")
# print(decomp(22) == "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19")
# print(decomp(25) == "2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23")
# print(decomp(79) == "2^74 * 3^36 * 5^18 * 7^12 * 11^7 * 13^6 * 17^4 * 19^4 * 23^3 * 29^2 * 31^2 * 37^2 * 41 * 43 * 47 * 53 * 59 * 61 * 67 * 71 * 73 * 79")
# print(decomp(98) == "2^95 * 3^46 * 5^22 * 7^16 * 11^8 * 13^7 * 17^5 * 19^5 * 23^4 * 29^3 * 31^3 * 37^2 * 41^2 * 43^2 * 47^2 * 53 * 59 * 61 * 67 * 71 * 73 * 79 * 83 * 89 * 97")
