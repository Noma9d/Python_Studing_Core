from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    res = 0
    for i in number_list:
        res += Decimal(i)

    result = res / Decimal(len(number_list))
    return result


print(decimal_average([3, 5, 77, 23, 0.57], 6))