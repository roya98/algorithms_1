

#Q1
def half_func(str):
    length = len(str)
    result = ""
    if length % 2 != 0:
        first = str[0: ((length //2) +1 )]
        second = str[((length //2) +1 ):]

    else:
        first = str[0: (length // 2)]
        second = str[(length // 2):]
    result = "".join(second + first)

    return result


string1 = 'bbbbbcaaaaa'
print(half_func(string1))


#Q2
def string_unique(str3):

    my_set = set()

    for character in str3:
        my_set.add(character)


    return len(str3) == len(my_set)






str3 = 'abcde'
print(string_unique(str3))




