from collections import UserDict
from validation import validate_phone_number
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def is_valid(self):
        return validate_phone_number(self.value)


class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
            pass
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        is_valid, error = phone.is_valid()

        if not is_valid:
            raise error

        if not self.find_phone(phone_number):
            self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [item for item in self.phones if item.value != phone_number]

    def edit_phone(self, old_number, new_number):
        is_valid, error = Phone(new_number).is_valid()

        if not is_valid:
            raise error

        found_phone = self.find_phone(old_number)

        if found_phone:
            found_phone.value = new_number

    def find_phone(self, phone_number):
        return next((item for item in self.phones if item.value == phone_number), None)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        name = record.name.value
        if name not in self.data.keys():
            self.data[name] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]
