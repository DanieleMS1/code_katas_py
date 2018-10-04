# King Arthur and his knights are having
# a New Years party. Last year Lancelot
# was jealous of Arthur, because Arthur
# had a date and Lancelot did not, and
# they started a duel.
#
# To prevent this from happening again,
# Arthur wants to make sure that there
# are at least as many women as men at
# this year's party. He gave you a list
# of integers of all the party goers.
#
# Arthur needs you to return true if he
# needs to invite more women or false
# if he is all set.

def invite_more_women(arr):
    return True if sum(arr) > 0 else False

#si poteva fare cosi

def invite_more_women(arr):
    return sum(arr) > 0


print(invite_more_women([1, -1, 1]),True)
print(invite_more_women([-1, -1, -1]),False)
print(invite_more_women([1, -1]),False)
print(invite_more_women([1, 1, 1]),True)
print(invite_more_women([]),False)
