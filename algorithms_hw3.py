
# Q1
def arithmetical_mean(l1):
    mean = sum(l1) / len(l1)
    list2 =[]

    for num in l1:
        if num < mean:
            list2.append(num)

    return list2


l2 = [1, 3, 5, 6, 4, 10, 2, 3]
print(arithmetical_mean(l2))


#Q2
def find_lowest(l1):

    lowest1 = l1[0]
    lowest2= l1[1]

    for num in l1[1:]:
        if num < lowest1:
            lowest1 = num

    if l1.count(lowest1) >= 2:
        lowest2 = lowest1


    else:
        for number in l1[1:]:
          if number < lowest2 and number != lowest1:
             lowest2 = number


    return lowest1, lowest2


a=[198, 3, 1, 9, 10, 9, 2]
print(find_lowest(a))