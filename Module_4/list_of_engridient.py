# ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]

def format_ingredients(items):
    f = ''
    if len(items) == 0:
        return f

    for i in items:
        if len(items) == 1:
            return str(items[0])
        elif len(items) == 2:
            return str(items[0]) + ' and ' + str(items[-1])
        elif i == items[-1]:
            return f[0:-2] +' and '+ str(items[-1])
        else:
            f += str(i) + ', '
        
a = format_ingredients([])


print(a)

