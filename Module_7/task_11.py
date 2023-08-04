def sequence_buttons(string:str):
    upper_string = string.upper()
    result = ''
    symbol = {
        '1':['.', ',', '?', '!', ':'],
        '2':['A', 'B', 'C'],
        '3':['D', 'E', 'F'],
        '4':['G', 'H', 'I'],
        '5':['J', 'K', 'L'],
        '6':['M', 'N', 'O'],
        '7':['P', 'Q', 'R', 'S'],
        '8':['T', 'U', 'V'],
        '9':['W', 'X', 'Y', 'Z'],
        '0':' '
    }

    for i in upper_string:
        for k, j in symbol.items():
            if i in j:
                index = j.index(i)
                result += k*(index + 1)
            else:
                continue
                
    return result



# print(sequence_buttons('Hello, World!'))
print(sequence_buttons('Hello,'))