def maxSequence(arr):
    max_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr), i, -1):
            total = sum(arr[i:j])
            if total > max_sum:
                max_sum = total
    return max_sum

#vediamo se riesco a stampare l'array [i:j] -> max_sum


def maxSequenceSubArray(arr):
    max_sum = 0
    max_array = []
    for i in range(len(arr)):
        for j in range(len(arr), i, -1):
            total = sum(arr[i:j])
            if total > max_sum:
                max_sum = total
                max_array = arr[i:j]
    return max_array







print(maxSequence([]), 0)
print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

print(maxSequenceSubArray([]), 0)
print(maxSequenceSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
