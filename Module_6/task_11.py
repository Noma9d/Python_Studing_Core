def get_credentials_users(path):
    with open(path, 'rb') as file:
        result = []
        for i in file:
            j = i.decode()
            j = j.replace('\n', '')
            result.append(j)
        
    return result

    
        
        
            


print(get_credentials_users('/home/nomad/Studing/Module_6/task_10.bin'))