# We have the following sequence:
#
# f(0) = 0
# f(1) = 1
# f(2) = 1
# f(3) = 2
# f(4) = 4;
# f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4) + f(n-5);
# Your task is to give the number of total values for
# the odd terms of the sequence up to the n-th term
# (included). (The number n (of n-th term) will be
# given as a positive integer)
#
# The values 1 (one) is the only that is duplicated i
# n the sequence and should be counted only once.

fib_cache = {
    0:0,
    1:1,
    2:1,
    3:2,
    4:4
}

def fib_5(n):
    if n in fib_cache:
        return fib_cache[n]
    fib_cache[n] = fib_5(n-1) + fib_5(n-2) + fib_5(n-3) + fib_5(n-4) + fib_5(n-5)
    return fib_cache[n]


def count_odd_pentaFib(n):
    odd_count = -1
    for i in range(n+1):
        if fib_5(i) % 2:
            odd_count += 1
    return odd_count



print(count_odd_pentaFib(5), 1)
print(count_odd_pentaFib(10), 3)
print(count_odd_pentaFib(15), 5)
print(count_odd_pentaFib(45), 15)

print(fibo(10))
