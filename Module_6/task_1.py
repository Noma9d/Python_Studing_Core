def total_salary(path):
    salary = []
    file = open(path)
    lines = file.readlines()
    for i in lines:
        j = i.replace('\n', '')
        salary.append(j)
    file.close()
    total = 0
    for j in salary:
        k = j.split(",")
        total +=float(k[1])

    return total



print(total_salary('/home/nomad/Studing/Module_6/task_1.txt'))