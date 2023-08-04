def real_len(text):
    symbol = [ '\n', '\f', '\r', '\t', '\v']
    real_text = list(text)
    for i in symbol:
        if  i in real_text:
            real_text.remove(i)
        else:
            continue

    length = len(real_text)
    return length






print(real_len('Al\nKdfe23\t\v.\r'))