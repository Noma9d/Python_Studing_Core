import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as file:
        write = csv.DictWriter(file, fieldnames=['name', 'email', 'phone', 'favorite'])
        write.writeheader()
        for item in contacts:
            write.writerow({'name':item['name'], 'email':item['email'], 'phone':item['phone'], 'favorite':item['favorite']})
            


def read_contacts_from_file(filename):
    contacts = []
    with open(filename, newline='') as file:
        contact = csv.DictReader(file)
        for item in contact:
            item['favorite'] = item['favorite'] == 'True'
            contacts.append(item)
    return contacts


write_contacts_to_file('eggs.csv', [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}])