# You will be given an array (a) and a value (x).
# All you need to do is check whether the
# provided array contains the value.
#
# Array can contain numbers or strings.
# X can be either. Return true if the array
# contains the value, false if not.

def check(seq, elem):
    if elem in seq:
        return True
    return False

#posso farlo piu piccolo
def check(seq, elem):
    return True if elem in seq else False

#visto che elem in seq è un valore True o False gia di suo
#si poteva fare anche cosi

def check(seq, elem):
    return elem in seq

print(check((66, 101), 66))
print(check((78, 117, 110, 99, 104, 117, 107, 115), 8))
print(check((101, 45, 75, 105, 99, 107), 107))
print(check((80, 117, 115, 104, 45, 85, 112, 115), 45))
print(check(('t', 'e', 's', 't'), 'e'))
print(check(("what", "a", "great", "kata"), "kat"))
print(check((66, "codewars", 11, "alex loves pushups"), "alex loves pushups"))
print(check(("come", "on", 110, "2500", 10, '!', 7, 15), "Come"))
print(check(("when's", "the", "next", "Katathon?", 9, 7), "Katathon?"))
print(check((8, 7, 5, "bored", "of", "writing", "tests", 115), 45))
print(check(("anyone", "want", "to", "hire", "me?"), "me?"))
