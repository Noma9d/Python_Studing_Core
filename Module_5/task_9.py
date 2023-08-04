def formatted_numbers():
    result = []
    result.append('|{0:^10}|{0:^10}|{0:^10}|'.format('decimal', 'hex', 'binary'))
    for i in range(0, 16):
        result.append('|{0:<10d}|{0:^10x}|{0:>10b}|'.format(i))
    return result


for el in formatted_numbers():
    print(el)