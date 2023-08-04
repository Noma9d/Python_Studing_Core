def add_employee_to_file(record, path):
    file = open(path, 'a')
    file.write(f'\n{record}')
    file.close()
    return file

add_employee_to_file('Drake Mikelsson, 20', '/home/nomad/Studing/Module_6/task_3.txt')