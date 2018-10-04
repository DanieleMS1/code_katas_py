# Calculate the product of all elements in an array.

def product(numbers):
    if not numbers:
        return None
    prod = 1

    for i in numbers:
        prod *= i

    return prod

print(product([5, 4, 1, 3, 9]), 540)
print(product([-2, 6, 7, 8]), -672)
print(product([10]), 10)
print(product([0, 2, 9, 7]), 0)
print(product(None), None)
print(product([]), None)
