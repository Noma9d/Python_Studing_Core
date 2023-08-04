def data_list(data):
    data.sort()
    data.pop(0)
    data.pop()
    return data


print(data_list([1,5,9,2,4,3,7,6]))