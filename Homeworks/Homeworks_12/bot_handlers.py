from bot_classes import Name, AdressBook, Record, Phone, Birthday

PHONE_BOOK = AdressBook() # Создаем словарь для записи данных при работе бота

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

def handler_help() -> str:
    return '''
    Commands:
    hello: prints Hello Message!
    add "user name" "user phone" : adds contact to the storage, if record already exist, adds new phone
    change "user name" "old phone" "new phone": change existing number to a new one
    delete phone "user name" "phone": removes specified phone from record
    show all: shows all contacts
    good, exit or close: ends the bot and saves the data to a file
    search: returns a list of contacts in which matches are found
    '''

def handler_hello():
    return 'How can I help you?'

@handler_error
def handler_add(user_name, phone_number):
    user_name = Name(user_name)
    phone_number = Phone(phone_number)
    record = Record(user_name, phone_number)
    if user_name.name in PHONE_BOOK.data:
        PHONE_BOOK[user_name.name].add_phone(phone_number)
        return f'User name {user_name.name} with phone number {phone_number.phone} add!!!'
    else:
        PHONE_BOOK.add_record(record)
        return f'{user_name.name} record added in your phone book'

@handler_error
def handler_change(user_name, new_phone_number): #Создаем ф-цию для изменения номера телефона существующего абонента
    user_name = Name(user_name)
    new_phone_number = Phone(new_phone_number)
    if user_name.name in PHONE_BOOK:
        PHONE_BOOK[user_name] = new_phone_number
        return f'Number of user name {user_name.name} have change.'
    else:
        return f'This is user name: {user_name.name} not in your phone book' #Выводим сообщение что абонент с таким именем отсутствует

@handler_error
def handler_phone(user_name): #Ф-ция для вывода номера телефона по имени
    user_name = Name(user_name)
    return f'Phone number for {user_name.name} : {PHONE_BOOK[user_name.name]}'

def show_all():
    result = ''
    for items, values in PHONE_BOOK.items():
        result += f'{items} : {values}\n'
    return result[:-1]

@handler_error
def handler_delete(name):
    name = Name(name)
    res = PHONE_BOOK.pop(name.name)
    return f'{res} contact was delete'
    
def handler_exit(file_name):
    PHONE_BOOK.save_records_to_file(file_name)
    exit('Good bye')

def handler_search(search_string):
    find_list = PHONE_BOOK.find_record(search_string)

    return find_list

HANDLERS = {
    'search':handler_search,
    'help':handler_help,
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
    
