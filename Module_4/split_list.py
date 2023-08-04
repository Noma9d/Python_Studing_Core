def split_list(grade):

    if len(grade) == 0:
        return ([], [])

    i = 0

    for item in grade:
        i += item

    sr = i/len(grade)
    
    first_list = []

    second_list = []

    for char in grade:
        
        if char <= sr:
            first_list.append(char)
        elif char > sr:
            second_list.append(char)
        


    return (first_list, second_list)


print(split_list([1, 2, 3, 4, 5]))