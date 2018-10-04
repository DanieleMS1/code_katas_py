# You get an array of numbers,
# return the sum of all of
# the positives ones.
#
# Example [1,-4,7,12]
# => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum,
# the sum is default to 0.


def positive_sum(arr):
    sum = 0
    for number in arr:
        if number > 0:
            sum += number

    return sum

#si poteva fare in una linea
#ma non conoscevo la funzione sum()

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

print(positive_sum([1,2,3,4,5]),15)
print(positive_sum([1,-2,3,4,5]),13)
print(positive_sum([-1,2,3,4,-5]),9)
print(positive_sum([]),0)
print(positive_sum([-1,-2,-3,-4,-5]),0)
