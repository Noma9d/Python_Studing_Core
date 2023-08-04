def lookup_key(data, value):

    valu = []

    for l, val in data.items():
        if val == value:
            valu.append(l)
            # valu += l


    return valu

f = lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2)

print(f)


