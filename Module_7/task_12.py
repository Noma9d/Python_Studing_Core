def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as file:
        file.write(f'\n{additional_info}')
        file.seek(0)

    with open(path, 'r') as file_read:
        file_read.seek(start_pos)
        return file_read.read() 
    
        
        
print(file_operations('/home/nomad/Studing/Module_6/task_1.txt', 'Alex', 2, '4'))