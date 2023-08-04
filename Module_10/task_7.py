class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


    def info(self):
        return {'name':self.name, 'age':self.age, 'address':self.address}



class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.owner = owner
        self.breed = breed
        
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return owner.info()
    

owner = Owner("Sherlock", 24, "London, 221B Baker Street")
dog = Dog("Simon", 10, "british", owner)

print(dog.who_is_owner())