import re


def find_all_emails(text):
    result = re.findall(r'[a-zA-Z]+[\w\.]+@[a-zA-Z0-9]+\.[a-z|A-Z]{2,}', text)


    return result

print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'))