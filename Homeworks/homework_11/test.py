from bot_classes import Name, AdressBook, Phone, Record, Birthday
from datetime import datetime, timedelta

# name = Name('Ivan')
# phone = Phone('380-(680)597777')
# birthday = Birthday('20/05/95')

# name1 = Name('Kate')
# phone1 = Phone('380-(680)598888')
# birthday1 = Birthday('03/04/98')

# name2 = Name('Viki')
# phone2 = Phone('380-(680)758965')
# birthday2 = Birthday('09/08/97')

# rec2 = Record(name2, phone2, birthday2)
# rec2.add_phone(Phone('+380680758965'))

# rec1 = Record(name1, phone1, birthday1)
# rec1.add_phone(Phone('+380678888'))

# rec = Record(name, phone, birthday)
# rec.add_phone(Phone('+380-680567777'))

# iter = AdressBook()
# iter.add_record(rec)
# iter.add_record(rec1)
# iter.add_record(rec2)

# for i in iter.iterator(1):
#     print(i)

# for i in iter.iterator(2):
#     print(i)
# print(rec.days_to_birthday())
# not_birth = Record(name, phone)
# print(name.name)
# print(phone.phone)
# print(birthday.date_birthday)
# print(not_birth.days_to_birthday()) 

b = Record(name=Name('Alex'), phone=Phone('+380-6(80)567777'))
print(b)
b.add_phone(Phone('+380-6(80)569999'))
print(b.phones[0]) # потрібно додати __str__ до Phone
# print(b.phones[0].phone) # бо значення лише можливо побачити з доступом
# print(b.name) # потрібно додати __str__ до Name
# print(b.name.name)
# b.add_phone(Phone('2895739'))
# b.add_phone(Phone('+38-6(80)5699'))
# print(b)

# print(b.phones[1].phone)
print(b.phones)
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