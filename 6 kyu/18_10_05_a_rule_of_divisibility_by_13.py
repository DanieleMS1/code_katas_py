# When you divide the successive powers of 10 by 13
# you get the following remainders of the integer divisions:
#
# 1, 10, 9, 12, 3, 4.
#
# Then the whole pattern repeats.
#
# Hence the following method: Multiply the right most
# digit of the number with the left most number in the
# sequence shown above, the second right most digit to the
# second left most digit of the number in the sequence.
# The cycle goes on and you sum all these products.
# Repeat this process until the sequence of sums is stationary.

def thirt(n):
    n_digits = [int(i) for i in str(n)][::-1]
    remainders_ten = (1,10,9,12,3,4)
    sum_of_digits, next_sum = 0, -1

    while sum_of_digits != next_sum :
        sum_of_digits, next_sum = 0, 0
        for i, item in enumerate(n_digits):
            multiplier = remainders_ten[i % len(remainders_ten)]
            sum_of_digits += item*multiplier
        digits_in_sum_of_digits = [int(i) for i in str(sum_of_digits)][::-1]
        for i, item in enumerate(digits_in_sum_of_digits):
            multiplier = remainders_ten[i % len(remainders_ten)]
            next_sum += item*multiplier
        n_digits = digits_in_sum_of_digits
    return sum_of_digits

#SI POTEVA FARE RICORSIVAMENTEEEEEEEEEEEEEEEEEEEEEEEEE

remainders = (1,10,9,12,3,4)
def thirt(n):
    n_digits = [int(i) for i in str(n)][::-1]
    tot = sum(c*remainders[i%6] for i, c in enumerate(n_digits))
    if tot == n:
        return n
    return thirt(tot)




print(thirt(8529), 79)
print(thirt(85299258), 31)
print(thirt(5634), 57)
print(thirt(1111111111), 71)
print(thirt(987654321), 30)
print(thirt(87), 87)
