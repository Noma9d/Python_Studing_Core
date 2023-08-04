import base64


def encode_data_to_base64(data):
    result = []
    for i in data:
        j = i.encode('utf-8')
        b_64j = base64.b64encode(j)
        res_j = b_64j.decode('utf-8')
        result.append(res_j)
    
    return result
    
    
        
        
        
print(encode_data_to_base64(['andry:uyro18890D', 'steve:oppjM13LL9e'])) #['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']