import re


def token_parser(s):
    j = re.findall(r'\d+|[-+*/()]', s)

    return j

            
print(token_parser('2+ 34 -5 * 3'))