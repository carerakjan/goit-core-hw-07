from collections import UserDict
from validation import validate_phone_number, validate_birthday
from datetime import datetime
from get_upcomig_birth import get_upcoming_birthdays


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

#Validation.for('birthday').validate()

class Birthday(Field):
    def __init__(self, value):
        _, error = validate_birthday(value)
        if error:
            raise error

        super.__init__(datetime.strptime(value, '%d.%m.%Y'))

    def __str__(self):
       return self.value.strftime('%Y.%m.%d')

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

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        name = record.name.value
        if name not in self.data.keys():
            self.data[name] = record

    def find(self, name, default) -> Record:
        return self.data.get(name, default)

    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]

    def add_birthday(self, name, birthday):
        record = self.find(name)
        if record:
            record.add_birthday(birthday)

    def show_birthday(self, name):
        record = self.find(name, f'There is no contact with name: {name}')
        return record.get('birthday', 'Contact has no birthday yet') if isinstance(Record) else record

    def birthdays(self):
        records = [{
            'name': rec.name,
            'birthday': rec.birthday.strftime('%Y.%m.%d')
        } for rec in self.data.values() if rec.birthday]
       
        return get_upcoming_birthdays(records)
    
    def __str__(self) -> str:
        return '\n'.join(self.data.values())
