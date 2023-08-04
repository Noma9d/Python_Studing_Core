def positive_values(list_payment):
    result = []
    for i in filter(lambda x: x > 0, list_payment):
        result.append(i)

    return result