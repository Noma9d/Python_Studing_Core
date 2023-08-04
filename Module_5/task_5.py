def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    phone_country_dict = {}
    sanitize_phone = []
    country_code = ['81', '65', '886', '380']
    for i in list_phones:
        i = str(i)
        sanitize_phone.append(sanitize_phone_number(i))
    for item in sanitize_phone:
        if item.find('81', 0, 2) != -1:
            phone_country_dict.setdefault('JP', []).append(item)
        elif item.find('65', 0, 2) != -1:
            phone_country_dict.setdefault('SG',[]).append(item)
        elif item.find('886', 0, 3) != -1:
            phone_country_dict.setdefault('TW', []).append(item)
        else:
            phone_country_dict.setdefault('UA', []).append(item)
    
    return phone_country_dict


    
    


print(get_phone_numbers_for_countries(['    +65(050)123-32- 34', '    +38(050)813-32- 34','    +81(050)123-32- 34']))