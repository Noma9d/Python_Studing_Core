def data_preparation(list_data):
    result = []
    for i in list_data:
        if len(i) <= 2:
            result.extend(i)
        else:
            i.sort()
            j = i[-1]
            k = i[0]
            i.remove(j)
            i.remove(k)
            result.extend(i)

    result.sort()
    result.reverse()
    return result


print(data_preparation([[1,2,3],[3,4], [5,6]]))