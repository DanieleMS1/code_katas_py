# You are going to be given a word.
# Your job is to return the middle
# character of the word. If the word's
# length is odd, return the middle character.
# If the word's length is even, return the
# middle 2 characters.

def get_middle(string):
    #odd
    if len(string) % 2:
        return string[int(len(string)/2)]
    #even
    return string[int(len(string)/2)-1] + string[int(len(string)/2)]





print(get_middle("middle"), "dd")
print(get_middle("testing"), "t")
print(get_middle("test"), "es")
print(get_middle("A"), "A")
print(get_middle("of"), "of")
