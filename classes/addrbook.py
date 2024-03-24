from collections import UserDict

from classes.addrbook_record import AddressBookRecord
from utils.birthday import get_upcoming_birthdays


class AddressBook(UserDict):
    def add_record(self, record: AddressBookRecord):
        name = record.name.value
        if name in self.data.keys():
            found_record = self.data[name]
            found_record.add_phone(record.phones[0].value)
        else:
            self.data[name] = record

    def find(self, name) -> AddressBookRecord:
        try:
            return self.data[name]
        except KeyError:
            raise Exception('Contact does not exist')

    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]

    def show_phones(self, name):
        record = self.find(name)
        return record.stringify_phones()

    def add_birthday(self, name, birthday):
        record = self.find(name)

        record.add_birthday(birthday)

    def show_birthday(self, name):
        record = self.find(name)
        return record.birthday or 'Contact has no birthday yet'

    def birthdays(self):
        records = [{
            'name': str(rec.name),
            'birthday': str(rec.birthday)
        } for rec in self.data.values() if rec.birthday]

        return '\n'.join(
            (f"Contact name: {item['name']}, "
             f"congratulation date: {item['congratulation_date']}") for item in get_upcoming_birthdays(records)
        ) or 'No upcoming birthdays'

    def __str__(self) -> str:
        return '\n'.join(str(record) for record in self.data.values()) or 'No contacts'
