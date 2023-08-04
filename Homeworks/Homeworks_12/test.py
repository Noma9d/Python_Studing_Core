from bot_classes import Name, AdressBook, Phone, Record, Birthday
from datetime import datetime, timedelta



b = Record(name=Name('Viktor'), phone=Phone('+380-6(80)567715'), birthday=Birthday('15/05/1995'))
b.add_phone(Phone('+380-6(80)569999'))
f = Record(name=Name('Viki'), phone=Phone('+380-6(80)567615'), birthday=Birthday('15/05/2002'))
d = Record(name=Name('Viksi'), phone=Phone('+380-661537615'), birthday=Birthday('15/10/2002'))
a = AdressBook()
a.add_record(d)
a.add_record(b)
a.add_record(f)
# print(a.data)

c = a.find_record('15')


print(c)




# print(b)
# print(b.phones)
# print(b.phones[0]) # потрібно додати __str__ до Phone
# print(b.phones[0].phone) # бо значення лише можливо побачити з доступом
# print(b.name) # потрібно додати __str__ до Name
# print(b.name.name)
# b.add_phone(Phone('2895739'))
# b.add_phone(Phone('+38-6(80)5699'))
# print(b)
# print(b.phones[1].phone)
# print(b.phones)
# b.name = Name(122222) # тут повинна бути викликано виключення
# print(b.name) # 
# print(b.name.name) # значення буде None
# b = Record(name=Name('Alex'), phone=Phone('+380-6(80)567777'))
# print(b)
# print(b.name) # потрібно додати __str__ до Name
# b.name = Name(122222) # тут повинна бути викликано виключення
# print(b.name) # 
# print(b.name.name) # значення буде None
# print(b.phones[0]) # потрібно додати __str__ до Phone
# b.add_phone(Phone('aaaaaa'))


