def all_sub_lists(data):
    result = [[]]
    for i in range(1, len(data)+1):
        start = 0
        last = start +i
        while last <= len(data):
            result.append(data[start:last])
            start += 1
            last += 1


    return result
    
        
            
print(all_sub_lists([1, 2, 3]))