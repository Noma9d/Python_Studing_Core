def sanitize_phone_number(phone):
    # phone = phone.strip()
    phone = list(phone)
    symbol = ['(',')','+','-', ' ']
    result = []
    for i in phone:
        if i in symbol:
            continue
        else:
            result.append(i)
    
    text = "".join(result)
    return text

print(sanitize_phone_number("    +38(050)123-32- 34"))