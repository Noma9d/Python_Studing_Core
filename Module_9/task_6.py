def generator_numbers(string=""):
    res = string.split(' ')
    result = []
    for i in res:
        j = i.removeprefix('$').removesuffix('.').removesuffix(',')
        if j.isdigit() == True:
            result.append(j)

    for item in result:
        yield item



def sum_profit(string):
    result = 0
    for i in generator_numbers(string):
        result += int(i)    
    
    return result
    
        
    


print(sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."))