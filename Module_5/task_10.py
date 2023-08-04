import re


def find_word(text, word):
    result_dict = {
        'result':'',
        'first_index':None,
        'last_index':None,
        'search_string':word,
        'string': text
    }

    j = re.search(word, text)
    if j == None:
        result_dict.update({'result':False})
    else:
        result_dict.update({'result':True})
        result_dict.update({'first_index':j.span()[0]})
        result_dict.update({'last_index':j.span()[1]})

    return result_dict


print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))