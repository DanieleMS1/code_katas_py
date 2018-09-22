# An isogram is a word that has no
# repeating letters, consecutive or
# non-consecutive. Implement a function
# that determines whether a string that
# contains only letters is an isogram.
# Assume the empty string is an isogram.
# Ignore letter case.
#
# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false


def is_isogram(string):
    chars = []
    for c in string:
        if c.lower() in chars:
            return False
        chars.append(c)
    return True

# posso farlo piu piccolo?


def is_isogram(string):
    chars = [c.lower() for c in string]
    for c in chars:
        if chars.count(c) > 1:
            return False
    return True

#si poteva fare in una linea con i set!
#un set è un insieme di tutti gli UNICI elementi di un oggetto
#esempio "daniele" -> [d,a,n,i,e,l]
#        "123432561" -> [1,2,3,4,5,6]

def is_isogram(string):
    return len(string) == len(set(string.lower()))

print(is_isogram("Dermatoglyphics"), True)
print(is_isogram("isogram"), True)
print(is_isogram("aba"), False)
print(is_isogram("moOse"), False)
print(is_isogram("isIsogram"), False)
print(is_isogram(""), True)
