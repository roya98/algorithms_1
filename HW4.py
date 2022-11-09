

#1
# [7, 3, 5, 6, 4, 10, 3, 2]
# Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(lst):

    for i in range(0, len(lst)):
        for k in range(i+1, len(lst)):
            if lst[i] % 2 != 0:
                odd = lst[i]
                if lst[k] % 2 == 0:
                    even = lst[k]
                    lst[i] = even
                    lst[k] = odd

    return lst


a1 = [7, 3, 5, 6, 4, 10, 3, 2]
print(even_first(a1))


# Q2


def increment_by_one(arr):
    for i in reversed(range(0, len(arr))):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        else:
            arr[i] = 0

    arr.insert(0,1)
    return arr


a = [1,2,9]
print(increment_by_one(a))
















