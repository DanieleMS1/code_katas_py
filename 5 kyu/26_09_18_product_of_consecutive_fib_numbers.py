# The Fibonacci numbers are the numbers in the following integer sequence (Fn):
# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
#
# F(n) * F(n+1) = prod.
#
# Your function productFib takes an integer (prod) and returns an array:
#
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.
#
# If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return
#
# [F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(m) being the smallest one such as F(m) * F(m+1) > prod.

fib_cache = {}


def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]

    if n < 2:
        value = n
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    fib_cache[n] = value
    return value


def productFib(prod):
    num = fibonacci(0)
    num_next = fibonacci(1)
    next = 2
    while num * num_next < prod:
        num = num_next
        num_next = fibonacci(next)
        next += 1

    return [num, num_next, True] if num * num_next == prod else [num, num_next, False]


print(productFib(4895), [55, 89, True])
print(productFib(5895), [89, 144, False])
