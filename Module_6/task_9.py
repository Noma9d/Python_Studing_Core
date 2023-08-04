def is_equal_string(utf8_string, utf16_string):
    u = utf8_string.decode()
    t = utf16_string.decode('utf-16')
    if u == t:
        return True
    else:
        return False
    
print(is_equal_string(b'utf', b'\xff\xfeu\x00t\x00f\x00'))