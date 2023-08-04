def get_recipe(path, search_id):
    result = {}
    with open(path, 'r') as file:
        for i in file:
            j = i.replace('\n', '')
            if j.find(search_id) != -1:
                k = j.split(',')
                result.update(id = k[0], name = k[1], ingredients = k[2:])
                return result
    return None

    
        
            
            
                
print(get_recipe('/home/nomad/Studing/Module_6/task_6.txt', '60b90c3b13067a15887e1ae4'))