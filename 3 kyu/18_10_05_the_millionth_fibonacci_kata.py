#fibonacci for very large n and negative n


def fib(n):
    pos_n = abs(n)
    even_neg = 1
    if (n < 0) and(n % 2 == 0):
        even_neg = -1
    len = 3
    array = [0,1,1]
    if len > 2:
        while len <= pos_n:
            array[len % 3] = array[(len - 1) % 3] + array[(len - 2) % 3]
            len += 1
    return even_neg * array[pos_n % 3]
