# A masked number is a string that
# consists of digits and one asterisk (*)
# that should be replaced by exactly one
# digit. Given a masked number s, find all
# the possible options to replace the asterisk
# with a digit to produce an integer divisible by 6.


def is_divisible_by_6(s):

    final_list = []
    for i in range(10):
        s_rep = s.replace("*", str(i))

        if int(s_rep) % 6 == 0:
            if s_rep[0] == "0" and s_rep != "0":
                s_rep = s_rep.replace("0", "", 1)

            final_list.append(s_rep)

    return final_list


print(is_divisible_by_6("1*0"), ["120", "150", "180"])
print(is_divisible_by_6("*"), ["0", "6"])
print(is_divisible_by_6("*1"), [])
print(is_divisible_by_6("*2"), ["12", "42", "72"])
print(is_divisible_by_6("81234567890*"), ["812345678904"])
print(is_divisible_by_6("41*"), ["414"])
print(is_divisible_by_6("*6"), ["6", "36", "66", "96"])
print(is_divisible_by_6("2345*345729"), [])
