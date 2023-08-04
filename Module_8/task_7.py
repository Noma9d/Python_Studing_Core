import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    result = []
    for i in cats:
        if isinstance(i, dict):
            result.append(Cat(nickname = i['nickname'], age = i['age'], owner = i['owner']))
        else:
            result.append({'nickname':i.nickname, 'age':i.age, 'owner':i.owner})

    return result

    
        
            
                    

print(convert_list([
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]))

print(convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]))