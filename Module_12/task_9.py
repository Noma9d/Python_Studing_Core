import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        result = Person(self.name, self.email, self.phone, self.favorite)
        result.name = copy.copy(self.name)
        result.email = copy.copy(self.email)
        result.phone = copy.copy(self.phone)
        result.favorite = copy.copy(self.favorite)
        return result
            

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        res = Contacts(self.filename, self.contacts)
        res.filename = copy.copy(self.filename)
        res.contacts = copy.copy(self.contacts)
        res.is_unpacking = copy.copy(self.is_unpacking)
        res.count_save = copy.copy(self.count_save)
        return res
        

    def __deepcopy__(self, memo):
        res = Contacts(self.filename, self.contacts)
        memo[id(res)] = res
        res.filename = copy.deepcopy(self.filename)
        res.contacts = copy.deepcopy(self.contacts)
        res.is_unpacking = copy.deepcopy(self.is_unpacking)
        res.count_save = copy.deepcopy(self.count_save)
        return res
        
        
        
        