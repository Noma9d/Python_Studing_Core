def read_employees_from_file(path):
    file = open(path, 'r')
    result = []
    lines = file.readlines()
    for i in lines:
        j = i.replace('\n', '')
        result.append(j)
    file.close()
    return result

    
    
    
    
        
print(read_employees_from_file('/home/nomad/Studing/Module_6/task_3.txt'))
