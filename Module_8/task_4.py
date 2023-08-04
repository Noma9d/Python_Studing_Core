from random import randrange


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return []
    
    result = []
    while len(result) != quantity:
        i = randrange(min, max + 1)
        if i in result:
            continue
        elif i == max and len(result) != quantity - 1:
            continue
        else:
            result.append(i)

    result.sort()
    return result


print(get_numbers_ticket(1, 10, 3))
        
            
            
                
            
            
    