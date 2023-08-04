from random import randint

def get_random_password():
    leng_password = 8
    result = ""
    for i in range(leng_password):
        result += str(chr(randint(40, 126)))

    return result
        
passwordd = get_random_password()

print(passwordd)

def is_valid_password(password):
    upper, lower, num = 0, 0, 0
    for i in password:

        if "A" <= i <= "Z":
            upper += 1
        if "a" <= i <= "z":
            lower += 1
        if "0" <= i <= "9":
            num +=1

    if len(password) == 8 and upper >= 1 and lower >= 1 and num >= 1:
        return True
    else:
        return False

print(is_valid_password(passwordd))

def get_password():
    passw = get_random_password()
    valid = is_valid_password(passw)
    print(passw)
    print(valid)
    count = 1
    while count <= 10:
        print(count)
        if valid == True:
            return passw
            break 
        else:
            passw = get_random_password()
            valid = is_valid_password(passw)
            print(passw)
            print(valid)
            count += 1
            continue
    
    return False


print(get_password())