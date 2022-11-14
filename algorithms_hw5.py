# Q1 Selection sort

def selection_sort_reversed(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_index]:
               max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


test_list = [4,1,2,20,9,11]
print(selection_sort_reversed(test_list))



def bubble_sort_reversed(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# test_list = [4,1,2,20,9,11]
print(bubble_sort_reversed(test_list))



def insertion_sort_reversed(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key

    return arr



#test_list = [4,1,2,20,9,11]
print(insertion_sort_reversed(test_list))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_array = arr[:middle]
    right_array = arr[middle:]
    return merge_arrays(merge_sort(left_array), merge_sort(right_array))
    # merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))





def merge_arrays(left_arr, right_arr):
    merged_array = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] >= right_arr[j]:
             merged_array.append(left_arr[i])
             i += 1
        else:
             merged_array.append((right_arr[j]))
             j += 1
    return merged_array


#test_list = [4,1,2,20,9,11]
print(merge_sort(test_list))
