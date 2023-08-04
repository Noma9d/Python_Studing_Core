def write_employees_to_file(employee_list, path):
    file = open(path, 'w')
    for i in employee_list:
        for j in i:
            file.write(f'{j}\n')
    file.close
    
                
    
        


print(write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]))