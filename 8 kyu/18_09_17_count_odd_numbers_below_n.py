# Given a number n, return the number of positive odd numbers below n, EASY!


def odd_count(n):

    if n % 2 == 0:
        return n / 2
    return (n - 1) / 2
