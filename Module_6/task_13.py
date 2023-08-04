import shutil


def create_backup(path, file_name, employee_residence):
    open_path = path + f'/{file_name}'
    with open(open_path, 'wb') as file:
        for i, j in employee_residence.items():
            res = f'{i} {j}' + '\n'
            b_res = res.encode()
            file.write(b_res)
    
    archive = shutil.make_archive('backup_folder', 'zip', path)

    return archive
    
        
            
print(create_backup('/home/nomad/Studing/Module_6', 'task_13.bin', {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'} ))