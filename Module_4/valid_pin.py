def is_valid_pin_codes(pin_codes):
    
    if len(pin_codes) == 0:
        return False
    

    for item in pin_codes:
        for j in item:
            try:
                int(j)
            except ValueError:
                return False

        if type(item) == str and len(item) == 4 and pin_codes.count(item) == 1:
            continue
        else:
            return False
        
        

    return True
    
        
            

print(is_valid_pin_codes(['1101', '9034', '0011','0011']))
            
        
            
    