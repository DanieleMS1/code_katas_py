# You have to create a function that takes a
# positive integer number and returns the next
# bigger number formed by the same digits:
#
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# If no bigger number can be composed using
# those digits, return -1:
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1
from itertools import permutations

#this works
def next_bigger(n):
    digits = [int(c) for c in str(n)]
    if digits == sorted(digits, reverse=True):
        return -1
    perm = sorted([p for p in permutations(digits) if list(p) > digits])
    return int(''.join(str(x) for x in perm[0]))

#this does not work
def next_bigger(n):
    digits = [int(c) for c in str(n)]
    number = [int(c) for c in str(n)]
    l = len(digits)
    if digits == sorted(digits, reverse=True):
        return -1

    i, j = l - 1, l - 2
    while True:
        if digits[i] > digits[j]:
            digits[i], digits[j] = digits[j], digits[i]
            digits[i:] = sorted(digits[i:])
            return int(''.join(str(x) for x in digits))
        else:
            i -= 1
            j -= 1

#this works but it's dumb
def next_bigger(n):
    digits = [int(c) for c in str(n)]
    if digits == sorted(digits, reverse=True):
        return -1
    next = n
    while True:
        next += 1
        if sorted(str(next)) == sorted(str(n)):
            return next

def next_bigger(n):
	n = str(n)[::-1]
	try:
		i = min(i+1 for i in range(len(n[:-1])) if n[i] > n[i+1])
		j = n[:i].index(min(a for a in n[:i] if a > n[i]))
		return int(n[i+1::][::-1]+n[j]+''.join(sorted(n[j+1:i+1]+n[:j])))
	except:
		return -1


print(next_bigger(12), 21)
print(next_bigger(513), 531)
print(next_bigger(2017), 2071)
print(next_bigger(414), 441)
print(next_bigger(144), 414)
print(next_bigger(9), -1)
print(next_bigger(1553), 3155)
print(next_bigger(5135), 5153)
print(next_bigger(19999999999999999999))
print(next_bigger(6))
