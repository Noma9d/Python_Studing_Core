def encode(data):
    if len(data) == 0:
        return []
    encoded = []
    symbol = data[0]
    count = 0
    for i in data:
        if i != symbol:
            break
        count += 1
    encoded.extend([symbol, count])
    encoded.extend(encode(data[count:]))
    return encoded

print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))