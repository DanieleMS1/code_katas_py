# You will be given a string (x)
# featuring a cat 'C' and a mouse 'm'.
# The rest of the string will be made
# up of '.'.
#
# You need to find out if the cat can
# catch the mouse from it's current
# position. The cat can jump over three
# characters. So:
#
# C.....m returns 'Escaped!' <--
# more than three characters between
#
# C...m returns 'Caught!' <-- as there
# are three characters between the two,
# the cat can jump.


def cat_mouse(string):

    index_cat = -1
    index_mouse = -1

    for c in string:
        if c == "C":
            index_cat = string.index(c)
        elif c == "m":
            index_mouse = string.index(c)

    if abs(index_cat - index_mouse) > 4:
        return "Escaped!"
    return "Caught!"


# si poteva fare cosi
# io pensavo potessero esserci anche cose del tipo C..m....
# la mia soluzione tiene conto anche ti cose cosi


def cat_mouse(string):
    return 'Escaped!' if string.count('.') > 3 else 'Caught!'


print(cat_mouse('C....m'), "Escaped!")
print(cat_mouse('C..m'), "Caught!")
print(cat_mouse('C.....m'), "Escaped!")
print(cat_mouse('C.m'), "Caught!")
print(cat_mouse('m...C'), "Caught!")
print(cat_mouse('C...m'), "Caught!")
# print(cat_mouse('C..m....'), "Caught!") <- questo è quello a cui avevo pensato
