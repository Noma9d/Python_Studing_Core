import json


def write_contacts_to_file(filename, contacts):
    data = {'contacts':contacts}
    with open(filename, 'w') as file:
        json.dump(data, file)
        


def read_contacts_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['contacts']
        
    
