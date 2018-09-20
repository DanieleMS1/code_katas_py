# We have two consecutive integers
# k1 and k2, k2 = k1 + 1
#
# We need to calculate the lowest
# integer n, such that: the values
# nk1 and nk2 have the same digits
# but in different order.


def find_lowest_int(k):

    # this is k_next = k + 1

    k_next = k + 1
    lowest_int = 1

    digits_k = []
    digits_k_next = [1]

    #let's multiply k and k_next

    while digits_k != digits_k_next:
        lowest_int += 1
        digits_k = [int(digit) for digit in str(k * lowest_int)]
        digits_k_next = [int(digit) for digit in str(k_next * lowest_int)]
        digits_k.sort()
        digits_k_next.sort()



    return lowest_int


print(find_lowest_int(325), 477)
print(find_lowest_int(599),2394)
print(find_lowest_int(855), 999)

print(find_lowest_int(1),125874)
print(find_lowest_int(100),8919)
print(find_lowest_int(1000),89919)
print(find_lowest_int(10000),899919)
