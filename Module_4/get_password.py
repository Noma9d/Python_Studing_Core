from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


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