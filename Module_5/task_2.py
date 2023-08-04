articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    result = []
    if letter_case == True:
        for item in articles_dict:
            for i in item.values():
                i = str(i)
                if key in i:
                    result.append(item)
    else:
        for item in articles_dict:
            for i in item.values():
                i = str(i)
                if key.title() in i or key.lower() in i:
                    result.append(item)
    
    return result

print(find_articles('Ocean'))
