def normal_name(list_name):
    res = []
    for i in map(lambda x: x.title(), list_name):
        res.append(i)
    return res



print(normal_name(["dan", "jane", "steve", "mike"]))
