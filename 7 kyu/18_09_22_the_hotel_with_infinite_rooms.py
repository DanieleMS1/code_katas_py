# The city of Darkishland has a strange
# hotel with infinite rooms. The groups
# that come to this hotel follow the
# following rules:
#
# At the same time only members of one
# group can rent the hotel.
#
# Each group comes in the morning of
# the check-in day and leaves the hotel
# in the evening of the check-out day.
#
# Another group comes in the very next
# morning after the previous group has
# left the hotel.
#
# A very important property of the incoming
# group is that it has one more member than
# its previous group unless it is the
# starting group. You will be given the
# number of members of the starting group.
#
# A group with n members stays for n days
# in the hotel. For example, if a group of
# four members comes on 1st August in the
# morning, it will leave the hotel on 4th
# August in the evening and the next group
# of five members will come on 5th August
# in the morning and stay for five days and
# so on.
#
# Given the initial group size you will have
# to find the group size staying in the hotel
# on a specified day.


# in pratica se la somma di tutte le persone che sono venute in albergo entro il giorno day è > day
# allora ritorno l'ultimo numero sommato

def group_size(initial_size, day):
    current_size = initial_size
    total_number_of_people = initial_size

    while total_number_of_people < day:
        current_size += 1
        total_number_of_people += current_size

    return current_size


# mi dice che il codice è troppo lento
# vediamo come migliorare
from math import floor


def group_size(initial_size, day):
    return floor((2 * day + initial_size * (initial_size - 1))**0.5 + 0.5)


print(group_size(1, 6), 3)
print(group_size(3, 10), 5)
print(group_size(3, 14), 6)
