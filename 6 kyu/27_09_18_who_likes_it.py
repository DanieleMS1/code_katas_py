# You probably know the "like"
# system from Facebook and other
# pages. People can "like" blog posts,
# pictures or other items. We want to
# create the text that should be
# displayed next to such an item.
#
# Implement a function likes :: [String] -> String,
# which must take in input array, containing
# the names of people who like an item.
# It must return the display text as shown in the examples:
#
# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
# For 4 or more names, the number in and 2 others simply increases.

def likes(names):
    if not names:
        return 'no one likes this'
    if len(names) == 1:
        return(names[0] + ' likes this')
    if len(names) == 2:
        return(names[0] + ' and ' + names[1] + ' like this')
    if len(names) == 3:
        return(names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this')
    return(names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this')

#penso si possa fare molto ma molto meglio pero cosi sembra funzionare

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    if len(names) == 1:
        return "%s likes this" % names[0]
    if len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    if len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)

#ok si possono usare i segnaposto in python

print(likes([]), 'no one likes this')
print(likes(['Peter']), 'Peter likes this')
print(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
