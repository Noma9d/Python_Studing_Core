from collections import UserDict

class Field:
    def __init__(self, value) -> None:
        self.value = value

class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.name = value

class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.phone = value

class AdressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
        
class Record():
    def __init__(self, name:Name, phone:Phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.add_phone(phone)

    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            raise ValueError('This is phone there is in your phone-book')
        
    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise KeyError('This is phone not in your phone-book')
        
    def edit_phone(self, current_phone, new_phone):
        if current_phone in self.phones:
            current_phone_index = self.phones.index(current_phone)
            self.phones.insert(current_phone_index, new_phone)
        else:
            raise ValueError('This is phone not in your phone-book')

