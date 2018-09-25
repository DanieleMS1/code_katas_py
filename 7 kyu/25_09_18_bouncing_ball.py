# You drop a ball from a given height.
# After each bounce, the ball returns
# to some fixed proportion of its
# previous height. If the ball bounces
# to height 1 or less, we consider it
# to have stopped bouncing. Return the
# number of bounces it takes for the
# ball to stop moving.

def bouncing_ball(initial, proportion):
    counter = 0
    bounce = initial
    while bounce > 1:
        bounce *= proportion
        counter += 1

    return counter


print(bouncing_ball(2, 0.5), 1)
print(bouncing_ball(4, 0.5), 2)
print(bouncing_ball(10, 0.1), 1)
print(bouncing_ball(100, 0.1), 2)
print(bouncing_ball(9, 0.3), 2)
print(bouncing_ball(30, 0.3), 3)
