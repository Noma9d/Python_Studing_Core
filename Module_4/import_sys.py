import sys


def parse_args():
    result = ""
    
    for arg in sys.argv:
        if arg.endswith(".py"):
            continue
        else:
            result += arg + ' '
        
    return result[0:-1]


print(parse_args())