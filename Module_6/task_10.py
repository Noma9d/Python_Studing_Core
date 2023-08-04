def save_credentials_users(path, users_info):
    with open(path, 'wb') as file:
        result = ''
        for i, j in users_info.items():
            res = f'{i}:{j}' + '\n'
            b_res = res.encode()
            file.write(b_res)
    
        
            
print(save_credentials_users('/home/nomad/Studing/Module_6/task_10.bin',{'andry':'uyro18890D', 'steve':'oppjM13LL9e'}))