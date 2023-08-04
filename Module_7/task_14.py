def to_indexed(source_file, output_file):
    with open(source_file, 'r') as file:
        res = file.readlines()
    
    with open(output_file, 'w') as new_file:
        r = 0
        for j in res:
            new_file.write(f'{r}: {j}')
            r += 1
        
    
    
        
    
        
print(to_indexed('/home/nomad/Studing/Module_6/task_1.txt', '/home/nomad/Studing/Module_7/task_14.txt'))     