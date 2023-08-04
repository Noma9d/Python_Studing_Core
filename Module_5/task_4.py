def is_check_name(fullname, first_name):
    if fullname.find(first_name) == 0:
        return True
    else:
        return False



print(is_check_name('Alexandr Smith', 'Alexandr'))