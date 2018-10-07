#very nice to read way

def iq_test(numbers):
    list_of_numbers = [int(i) for i in numbers.split(' ')]
    first_three = list_of_numbers[:3]
    even, odd = 0, 0
    for i in first_three:
        if i % 2:
            odd += 1
        else:
            even += 1

    if odd > even:
        for number in list_of_numbers:
            if number % 2 == 0:
                return list_of_numbers.index(number) + 1
    else:
        for number in list_of_numbers:
            if number % 2 == 1:
                return list_of_numbers.index(number) + 1

#cool more concise way
def iq_test(numbers):
    parity_list = [int(i) % 2 for i in numbers.split(' ')]
    return parity_list.index(0) + 1 if parity_list.count(1) > 1 else parity_list.index(1) + 1
#trashy 1 liner
def iq_test(numbers):
    return [int(i) % 2 for i in numbers.split(' ')].index(0) + 1 if [int(i) % 2 for i in numbers.split(' ')].count(1) > 1 else [int(i) % 2 for i in numbers.split(' ')].index(1) + 1

print(iq_test("2 4 7 8 10"),3)
print(iq_test("1 2 2"), 1)
