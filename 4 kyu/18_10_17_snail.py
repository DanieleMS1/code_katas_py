# Given an n x n array, return the array elements
# arranged from outermost elements to the middle
# element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
from random import randint

def snail(array):
    return list(array[0]) + snail(list(zip(*array[1:]))[::-1]) if array else []

d = 10000
array = [[randint(1,9) for x in range(d)] for y in range(d)]

for row in array:
    print(row)
print(snail(array))
