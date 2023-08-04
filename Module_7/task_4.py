def is_integer(s):
    
    s = s.strip()
    if len(s) == 0:
        return False
    elif not s[1:].isdigit():
        return False
    else:
        return True

print(is_integer(' -123 '))