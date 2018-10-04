# Deoxyribonucleic acid (DNA) is
# a chemical found in the nucleus
# of cells and carries the
# "instructions" for the development
# and functioning of living organisms.
#
# If you want to know more
# http://en.wikipedia.org/wiki/DNA
#
# In DNA strings, symbols "A" and "T"
# are complements of each other, as "C"
# and "G". You have function with one
# side of the DNA (string, except for Haskell);
# you need to get the other complementary
# side. DNA strand is never empty or there
# is no DNA at all (again, except for Haskell).
# DNA_strand ("ATTGC") return "TAACG"
# DNA_strand ("GTAT") return "CATA"


def DNA_strand(dna):
    dict = {
        'A':'T',
        'T':'A',
        'C':'G',
        'G':'C'
    }

    complement = ''
    for c in dna:
        complement += dict[c]

    return complement

#posso farlo piu piccolo?
def DNA_strand(dna):
    dict = {
        'A':'T',
        'T':'A',
        'C':'G',
        'G':'C'
    }
    complement = ''.join([dict[c] for c in dna])
    return complement
#ancora piu condensato
def DNA_strand(dna):
    dict = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join([dict[c] for c in dna])





print(DNA_strand("AAAA"),"TTTT")
print(DNA_strand("ATTGC"),"TAACG")
print(DNA_strand("GTAT"),"CATA")
