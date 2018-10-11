# This time we want to write calculations using
# functions and get the results. Let's have a look at some examples:
#
# JavaScript:
#
# seven(times(five())); // must return 35
# four(plus(nine())); // must return 13
# eight(minus(three())); // must return 5
# six(dividedBy(two())); // must return 3
# Ruby:
#
# seven(times(five)) # must return 35
# four(plus(nine)) # must return 13
# eight(minus(three)) # must return 5
# six(divided_by(two)) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following
# mathematical operations: plus, minus, times, dividedBy
# (divided_by in Ruby)
# Each calculation consist of exactly one operation
# and two numbers
# The most outer function represents the left operand,
# the most inner function represents the right operand
# Divison should be integer division, e.g
# eight(dividedBy(three()))/eight(divided_by(three)) should return 2, not 2.666666...

#I did not solve this but i'm learning from someone else's solution

def zero(*args):  return eval('0' + args[0]) if len(args) == 1 else '0'
def one(*args):   return eval('1' + args[0]) if len(args) == 1 else '1'
def two(*args):   return eval('2' + args[0]) if len(args) == 1 else '2'
def three(*args): return eval('3' + args[0]) if len(args) == 1 else '3'
def four(*args):  return eval('4' + args[0]) if len(args) == 1 else '4'
def five(*args):  return eval('5' + args[0]) if len(args) == 1 else '5'
def six(*args):   return eval('6' + args[0]) if len(args) == 1 else '6'
def seven(*args): return eval('7' + args[0]) if len(args) == 1 else '7'
def eight(*args): return eval('8' + args[0]) if len(args) == 1 else '8'
def nine(*args):  return eval('9' + args[0]) if len(args) == 1 else '9'

def plus(*args):       return '+' + args[0]
def minus(*args):      return '-' + args[0]
def times(*args):      return '*' + args[0]
def divided_by(*args): return '//' + args[0]



print(seven(times(five())), 35)
print(four(plus(nine())), 13)
print(eight(minus(three())), 5)
print(six(divided_by(two())), 3)

#   six(plus(five()))
#
#   five() -> '5'
#   plus('5') -> '+5'
#   six('+5') -> eval('6+5') -> 11

#   so eval(str) return the result of the math inside the string as if the string was not there
