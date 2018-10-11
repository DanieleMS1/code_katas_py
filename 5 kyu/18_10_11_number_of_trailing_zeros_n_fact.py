# reusing part of the code i used to solve factorial decomposition

from math import factorial


def zeros(n):

    n_fact = factorial(n)
    total_zeros = 0
    n_fact_list = list(str(n_fact))
    while n_fact_list[-1] == '0':
        total_zeros += 1
        n_fact_list.pop()

    return total_zeros

#not fast enough


def zeros(n):

    total_zeros = 0
    for i in range(1, n + 1):
        k = i
        while(k % 5 == 0):
            total_zeros += 1
            k /= 5
    return total_zeros

#not fast enough

def zeros(n):

    total_zeros = 0
    pow_of_five = 5
    while (n / pow_of_five >= 1):
        total_zeros += n // pow_of_five
        pow_of_five *= 5

    return total_zeros


print(zeros(0), 0, "Testing with n = 0")
print(zeros(6), 1, "Testing with n = 6")
print(zeros(30), 7, "Testing with n = 30")
print(zeros(125), 7, "Testing with n = 30")
