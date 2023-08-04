from bot_classes import Name, AdressBook, Field, Record, Phone

PHONE_BOOK = {} # Создаем словарь для записи данных при работе бота

#Создаем декоратор который используется для отлова ошибок
def handler_error(func): 

    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return 'Contacts not found'
        except ValueError:
            return 'Invalid input ValueError'
        except IndexError:
            return 'Invalid input IndexError'
        except TypeError:
            return 'Invalid input TypeError'

    return wrapper

def handler_hello():
    return f'How can I help you?'

@handler_error
def handler_add(user_name, phone_number):
    PHONE_BOOK[user_name] = phone_number
    return f'User name {user_name} with phone number {phone_number} add!!!'

@handler_error
def handler_change(user_name, new_phone_number): #Создаем ф-цию для изменения номера телефона существующего абонента
    if user_name in PHONE_BOOK:
        PHONE_BOOK[user_name] = new_phone_number
        return f'Number of user name {user_name} have change.'
    else:
        return f'This is user name: {user_name} not in your phone book' #Выводим сообщение что абонент с таким именем отсутствует

@handler_error
def handler_phone(user_name): #Ф-ция для вывода номера телефона по имени
    return f'Phone number for {user_name} : {PHONE_BOOK[user_name]}'

def show_all():
    result = ''
    for items, values in PHONE_BOOK.items():
        result += f'{items} : {values}\n'
    return result[:-1]

@handler_error
def handler_delete(name):
    res = PHONE_BOOK.pop(name)
    return f'{res} contact was delete'
    
def handler_exit():
    exit('Good bye')

HANDLERS = {
    'hello':handler_hello,
    'add':handler_add,
    'change':handler_change,
    'phone':handler_phone,
    'show all':show_all,
    'delete':handler_delete,
    'good':handler_exit,
    'exit':handler_exit,
    'close':handler_exit
}
    
