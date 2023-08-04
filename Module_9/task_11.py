from functools import reduce


def sum_numbers(numbers):
    result = reduce((lambda x, y: x + y), numbers)
    return result 


print(sum_numbers([3, 4, 6, 9, 34, 12]))