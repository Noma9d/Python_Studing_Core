def format_phone_number(func):
    def wrapper(phone):
        result = func(phone)
        if len(result) == 12:
            result = '+' + result
        else:
            result = '+38' + result
        return result
    return wrapper
        

@format_phone_number
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


print(sanitize_phone_number('     0503451234'))