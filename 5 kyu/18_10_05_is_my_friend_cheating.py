# A friend of mine takes a sequence of numbers
# from 1 to n (where n > 0).
# Within that sequence, he chooses two numbers, a and b.
# He says that the product of a and b should be equal
# to the sum of all numbers in the sequence, excluding a and b.
# Given a number n, could you tell me the numbers
# he excluded from the sequence?

def removNb(n):
    nums = [i for i in range(1, n + 1)]
    tot_num = (n*(n+1))/2 #gauss is my god
    list_final = []
    i, j = 0, len(nums)-1
    product, summation = -1,-1

    while product != tot_num - summation:
        product, summation = nums[i]*nums[j], nums[i]+nums[j]
        if product < tot_num - summation:
            i += 1
        elif product > tot_num - summation:
            j -= 1
        else:
            if (nums[i],nums[j]) not in list_final:
                list_final.append((nums[i],nums[j]))
                list_final.append((nums[j],nums[i]))
                i+=1
                j-=1
                product, summation = nums[i]*nums[j], nums[i]+nums[j]
        if i == j:
            break

    return sorted(list_final)




#
# my thought process
#
#
#
# i = k, j = m -- i*j = k*m -- i+j = k+m -- i*j  != (==) sum - k+m = sum - k+m
# sum - k+m > i*j shift i up
# sum - k+m < i*j shift j down
# sum - k+m = i*j return(i, j)
#
# Example with n  = 10
# 1,2,3,4,5,6,7,8,9,10 -- sum = 55
#
# i = 1, j = 10
#
# i = 1, j = 10 -- i*j = 10 -- i+j = 11 -- 10  != sum - 11 = 44
# 44 > 10 shift i up
# i = 2, j = 10 -- i*j = 20 -- i+j = 12 -- 20  != sum - 12 = 43
# 43 > 20 shift i up
# i = 3, j = 10 -- i*j = 30 -- i+j = 13 -- 30  != sum - 13 = 42
# 42 > 30 shift i up
# i = 4, j = 10 -- i*j = 40 -- i+j = 14 -- 40  != sum - 14 = 41
# 41 > 40 shift i up
# i = 5, j = 10 -- i*j = 50 -- i+j = 15 -- 50  != sum - 15 = 40
# 40 < 50 shift j down
# i = 5, j = 9 -- i*j = 45 -- i+j = 14 -- 45  != sum - 14 = 41
# 41 < 45 shift j down
# i = 5, j = 8 -- i*j = 40 -- i+j = 13 -- 40  != sum - 13 = 42
# 42 > 40 shift i up
# i = 6, j = 8 -- i*j = 48 -- i+j = 14 -- 48  != sum - 14 = 41
# 48 > 41 shift j down
# i = 6, j = 7 -- i*j = 42 -- i+j = 13 -- 42  == sum - 13 = 42
# 42 = 42 return(i,j)

print(removNb(100), [])
print(removNb(26), [(15, 21), (21, 15)])
