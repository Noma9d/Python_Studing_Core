def get_cats_info(path):
    result = []
    with open(path, 'r') as file:
        for i in file:
            j = i.replace('\n', '')
            k = j.split(',')
            result.append({'id':k[0], 'name':k[1], 'age':k[2]})
            

    return result
        
            
            
    
print(get_cats_info('/home/nomad/Studing/Module_6/task_5.txt'))