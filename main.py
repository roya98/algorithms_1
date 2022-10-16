

# Q1
#compute the sum of digits in all numbers from 1 to n

def sum_digits(n):
    result =0
    for i in range (1, n+1):
        result += i

    return result


a= sum_digits(5)
print(a)


#Q2
#Find max number

def find_max_numbers(n1,n2,n3):
    max = n1
    if n2 > max:
        max = n2
        if n3 > max:
          max = n3
    elif n3 > max:
        max = n3

    return max


print(find_max_numbers(5, 44, 24))


#Q3
#count odd and even

def count_odd_even(n):
    odd =0
    even =0

    number = n
    remainder = number % 10
    while number != 0:


            remainder = number % 10
            number = number // 10

            if remainder % 2 == 0:

                even = even +1

            else:

                odd = odd +1



    return odd, even


print(count_odd_even(34560))











