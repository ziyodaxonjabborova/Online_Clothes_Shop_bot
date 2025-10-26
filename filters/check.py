import re

def is_valid_fullname(name):
    name = name.strip()
    pattern = r'^[A-Za-zА-Яа-яЁё\s]{2,}$'
    return bool(re.fullmatch(pattern, name))



def is_valid_phone(phone: str) -> bool:
    phone = phone.strip()
    pattern = r'^(?:\+998|998|8|9)\d{8,9}$'
    return bool(re.fullmatch(pattern, phone))

