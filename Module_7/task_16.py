def decode(data:list):
    result = []
    if len(data) == 0:
        return []
    else:
        for i in range(0, data[1]):
            result.append(data[0])
        data.remove(data[1])
        data.remove(data[0])
        result.extend(decode(data))
    return result

        
print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))