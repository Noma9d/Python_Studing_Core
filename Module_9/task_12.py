from functools import reduce


def amount_payment(payment):
    result = reduce((lambda x, y: x + y if y > 0 else x), payment, 0)
    return result



print(amount_payment([1, -3, 4, 5]))