# The new "Avengers" movie has
# just been released! There are
# a lot of people at the cinema
# box office standing in a huge
# line. Each of them has a single
# 100, 50 or 25 dollars bill.
# An "Avengers" ticket costs 25 dollars.
#
# Vasya is currently working as a
# clerk. He wants to sell a ticket
# to every single person in this line.
#
# Can Vasya sell a ticket to each
# person and give the change if he
# initially has no money and sells
# the tickets strictly in the order
# people follow in the line?
#
# Return YES, if Vasya can sell a ticket
# to each person and give the change with
# the bills he has at hand at that moment.
# Otherwise return NO.


def tickets(people):
    # check if first item is 25 if not return "NO"
    if people[0] != 25:
        return "NO"
    # we have 25 dollars now
    # cash register
    cash_register = [[25, 1], [50, 0], [100, 0]]
    # we already took person 0 money
    for person in people[1:]:
        # if person is 25 no change
        if person == 25:
            cash_register[0][1] += 1
        # if person is 50 the only way to give change is with a 25
        elif person == 50:
            # check if we have 25, if not return "NO"
            if cash_register[0][1] == 0:
                return "NO"
            # else give the 25 back as change and take the 50
            cash_register[0][1] -= 1
            cash_register[1][1] += 1
        # if a person is 100 there are 2 ways to give change (25,25,25) or (25,50)
        else:
            # in either case i need a 25
            if cash_register[0][1] == 0:
                return "NO"
            # if i have a 25 i need to check if i have either a 50 or 2 other 25
            if cash_register[0][1] < 3 and cash_register[1][1] == 0:
                return "NO"
            # since 25s have more use, let's prioritize giving back 50s
            if cash_register[1][1] > 0:
                cash_register[0][1] -= 1
                cash_register[1][1] -= 1
                cash_register[2][1] += 1
            # if we cant we have to give back 25s
            else:
                cash_register[0][1] -= 3
                cash_register[2][1] += 1
    return "YES"
# facciamolo con un dizionario
# e controlliamo subito se abbiamo un 25!


def tickets(people):

    if people[0] != 25:
        return "NO"

    cash_register = {
        25: 1,
        50: 0,
        100: 0
    }

    for person in people[1:]:
        if person == 25:
            cash_register[25] += 1
        else:
            if cash_register[25] == 0:
                return "NO"
            if person == 50:
                cash_register[25] -= 1
                cash_register[50] += 1
            else:
                if cash_register[25] < 3 and cash_register[50] == 0:
                    return "NO"
                if cash_register[50] > 0:
                    cash_register[25] -= 1
                    cash_register[50] -= 1
                    cash_register[100] += 1
                else:
                    cash_register[25] -= 3
                    cash_register[100] += 1
    return "YES"


print(tickets([25, 100]), "NO")
print(tickets([25, 25, 50]), "YES")
print(tickets([25, 25, 25, 25, 50, 100, 50]), "YES")
