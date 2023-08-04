def sanitize_file(source, output):
    result = ''
    with open(source, 'r') as file:
        for i in file:
            for j in i:
                if j.isdigit():
                    continue
                else:
                    result += str(j)
    with open(output, 'w') as fh:
        fh.write(result)
    
sanitize_file('/home/nomad/Studing/Module_6/task_7.txt', '/home/nomad/Studing/Module_6/task_7.txt')