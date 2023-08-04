def make_request(keys, values):
    result = {}
    if len(keys) == len(values):
        for i, j in zip(keys, values):
            result[i] = j
    else:
        return result
    
    return result

    
        
print(make_request(['a', 'c'], ['f', 'h']))
        
    
