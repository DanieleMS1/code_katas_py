# Your friend advised you to see a new performance in
# the most popular theater in the city. He knows a lot
# about art and his advice is usually good, but not this
# time: the performance turned out to be awfully dull.
# It's so bad you want to sneak out, which is quite simple,
# especially since the exit is located right behind your
#  row to the left. All you need to do is climb over
#  your seat and make your way to the exit.
#
# The main problem is your shyness: you're afraid that
# you'll end up blocking the view (even if only for a
# couple of seconds) of all the people who sit behind
# you and in your column or the columns to your left.
# To gain some courage, you decide to calculate the
# number of such people and see if you can possibly
# make it to the exit without disturbing too many people.
#
# Given the total number of rows and columns in the
# theater (nRows and nCols, respectively), and the
# row and column you're sitting in, return the
# number of people who sit strictly behind you
# and in your column or to the left, assuming all
# seats are occupied.


def seats_in_theater(tot_cols, tot_rows, col, row):
    return ((tot_cols - col + 1) * (tot_rows - row))


# print(seats_in_theater(16, 11, 5, 3))
# print(seats_in_theater(1, 1, 1, 1))
# print(seats_in_theater(13, 6, 8, 3))


# Test.describe("Basic Tests")
# Test.assert_equals(seats_in_theater(16,11,5,3) , 96)
# Test.assert_equals(seats_in_theater(1,1,1,1) , 0)
# Test.assert_equals(seats_in_theater(13,6,8,3) , 18)
# Test.assert_equals(seats_in_theater(60,100,60,1) , 99)
# Test.assert_equals(seats_in_theater(1000,1000,1000,1000) , 0)
