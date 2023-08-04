def save_applicant_data(source, output):
    result = ''
    for i in source:
        for j in i.values():
           j = str(j)
           result += j + ','
        
        result =result[0:-1] + '\n'
        
    
    with open(output, 'w') as file:
        file.write(result)
    
    return result[0:-1]

print(save_applicant_data([{"name": "Kovalchuk Oleksiy","specialty": 301,"math": 175,"lang": 180,"eng": 155,}, 
                           {"name": "Ivanchuk Boryslav","specialty": 101,"math": 135,"lang": 150,"eng": 165,}, 
                           {"name": "Karpenko Dmytro","specialty": 101,"math": 135,"lang": 150,"eng": 165,}],'/home/nomad/Studing/Module_6/task_8.txt'))
        
            
                
            