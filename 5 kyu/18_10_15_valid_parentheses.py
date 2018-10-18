# Write a function called that takes a string of
# parentheses, and determines if the order of the
# parentheses is valid. The function should return
# true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100
#
# Along with opening (() and closing ())
# parenthesis, input may contain any valid
# ASCII characters. Furthermore, the input
# string may be empty and/or not contain any
# parentheses at all. Do not treat other forms
# of brackets as parentheses (e.g. [], {}, <>).

#metodo stupido! ma ne ho trovato uno molto ma molto meglio
def valid_parentheses(string):
    # tolgo tutto quello che non sono parentesi
    array = []
    copy_array = []
    for c in string:
        array.append(c)
        copy_array.append(c)

    for item in copy_array:
        if not (item == '(' or item == ')'):
            del array[array.index(item)]

    new_string = ''.join(array)
    new_string  = new_string.replace('()','')
    array = []
    for c in new_string:
        array.append(c)

    if not array:
        return True
    if array[0] == ')' or array[-1] == '(':
        return False

    return valid_parentheses(''.join(array[1:-1]))


#meglio cosi, meno codice, meno iterazioni
def valid_parentheses(string):

    for c in string:
        if not (c == '(' or c == ')'):
            string = string.replace(c, '')

    string = string.replace('()','')
    if not string:
        return True
    if string[0] == ')' or string[-1] == '(':
        return False

    return valid_parentheses(string[1:-1])




print(valid_parentheses("  ("),False)
print(valid_parentheses(")test"),False)
print(valid_parentheses(""),True)
print(valid_parentheses("hi())("),False)
print(valid_parentheses("hi(hi)()"), True)
