def get_employees_by_profession(path, profession):
    with open(path, 'r') as file:
        lines = file.readlines()
        result = []
        for i in lines:
            if i.find(profession) != -1:
                k = i.replace(f' {profession}\n', '')
                result.append(k)

        res = ' '.join(result)
            
    
    return res
        
    
    
        
            
    



print(get_employees_by_profession('/home/nomad/Studing/Module_6/task_1.txt', 'cook'))