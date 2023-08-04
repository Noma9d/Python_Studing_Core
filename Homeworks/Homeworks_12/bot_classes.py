import re
import pickle
from itertools import groupby
from datetime import date, datetime
from collections import UserDict


class Name():
    def __init__(self, name:str) -> None:
        self.__name = None
        self.name = name

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name:str):
        assert not isinstance(name, int), 'Name must be a string'
        if isinstance(name, str) and 2 <= len(name) <= 16 and name.isalpha():
            name = name.lower().capitalize()
            self.__name = name

    def __str__(self):
        return f'{self.name}'


class Phone():
    def __init__(self, phone) -> None:
        self.phone = phone
    
    def normalize(self, phone:str) -> str:
        phone = (
            phone.strip()
                .removeprefix("+")
                .replace("(", "")
                .replace(")", "")
                .replace("-", "")
                )
        return phone

    def validate(self, phone:str) -> str:

        if phone.isdigit():
                        
            if len(phone) == 12:
                phone = '+' + phone
                return phone
            elif len(phone) == 10 and phone[0:1] == '38':
                phone = '+38' + phone
                return phone
            else:
                raise ValueError('Phone must have 10 or 12 digits')
        else:
            raise ValueError('Phone must be a digit')
        
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone:str):
        phone = self.normalize(phone)
        phone = self.validate(phone)
        self.__phone = phone



    def __str__(self) -> str:
        return f'{self.phone}'
    
    def __repr__(self) -> str:
        return f'{self.phone!r}'

class Birthday():
    def __init__(self, value) :
        self.__date_birthday = None
        self.date_birthday = value

    @property
    def date_birthday(self):
        return self.__date_birthday.strftime("%d-%m-%Y")
    
    @date_birthday.setter
    def date_birthday(self, value: str):
        day, month, year = map(int, re.split(r"[-|_|\\|/]", value))
        date_birthday = date(year, month, day)
        if date_birthday >= date.today():
            raise ValueError('You write incorect date of birthday')
        self.__date_birthday = date_birthday

    def __str__(self) -> str:
        return f'{self.date_birthday}'
        

class Record():
    def __init__(self, name:Name, phone:Phone = None, birthday:Birthday = None) -> None:
        self.name = name
        self.birthday = birthday
        self.phones = []
        if phone:
            self.phones.append(phone)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: Name):
        self.__name = name

    @property
    def phones(self):
        return self.__phones

    @phones.setter
    def phones(self, phones):
        self.__phones = phones

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday: Birthday):
        self.__birthday = birthday

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
            self.phones.pop(current_phone_index)
            self.phones.insert(current_phone_index, new_phone)
        else:
            raise ValueError('This is phone not in your phone-book')
        
    def days_to_birthday(self):
        if self.birthday:
            today = datetime.today()
            days, month, year = self.birthday.date_birthday.split('-')
            if int(month) >= today.month:
                birthd = datetime(year = today.year, day=int(days), month=int(month))
                days_to_birthday = birthd - today
            else:
                birthd = datetime(year = today.year + 1, day=int(days), month=int(month))
                days_to_birthday = birthd - today
        else:
            return 'You are not input date of birthday from tjis contact'
        
        return days_to_birthday
    
    def __str__(self) -> str:
        str_phones = ", ".join(list(map(str, self.phones)))
        if self.phones and self.birthday:
            return f'Name of contact {self.name}. Phone of contact: {str_phones}. Birthday of contact: {self.birthday}'
        elif self.phones:
            return f'Name of contact {self.name}. Phone of contact: {str_phones}.'
        
    def __repr__(self) -> str:
        return f'{self.phones}, {self.birthday}'
        

class AdressBook(UserDict):

    def __init__(self) -> None:
        super().__init__()
        self.index = 1


    def add_record(self, record):   
        self.data[record.name.name] = record

    def iterator(self, n_items):
        keys = list(self.data.keys())
        for rec in self.data.values():
            name = rec.name
            
        while self.index <= n_items:
            try:
                yield f'{keys[self.index - 1]}:{self.data[keys[self.index - 1]]}'
                self.index += 1
            except IndexError:
                print('Your phone book is too shirt')
                self.index = 0
                break

    def find_record(self, search_string:str = ''):
        result = []
        search_string = search_string.lower()

        for name, values in self.data.items():
 
            phone = ", ".join(list(map(str, values.phones)))
            birthday = str(values.birthday)
            if search_string in name.lower():
                result.append(f'{values}')

            if search_string in phone:
                result.append(f'{values}')

            if search_string in birthday:
                result.append(f'{values}')

        sort_result = [el for el, _ in groupby(result)]
        return sort_result
            
    def save_records_to_file(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.data, file)

    def read_records_from_file(self, filename:str):
        try:
            with open(filename, "rb") as file:
                content = pickle.load(file)
                self.data.update(content)
        except FileNotFoundError:
            pass