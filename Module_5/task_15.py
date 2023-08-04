import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r'(?:http://|https://)\w+(?:\.\w+\.[a-z|A-Z]+|\w+\.[a-z|A-Z]+)', text)
    for match in iterator:
        result.append(match.group())
    return result


print(find_all_links('https://www.google.com https://www.facebook.com https://github.com http://gith_1.com'))