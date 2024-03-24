from collections import UserDict

from classes.addrbook_record import AddressBookRecord
from utils.birthday import get_upcoming_birthdays


class AddressBook(UserDict):
    def add_record(self, record: AddressBookRecord):
        self.data[str(record.name)] = record

    def find(self, name) -> AddressBookRecord:
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]

    def get_congratulation_list(self):
        to_dict = [vars(rec) for rec in self.data.values() if rec.birthday]
        return get_upcoming_birthdays(to_dict)

    def __str__(self) -> str:
        return '\n'.join(str(record) for record in self.data.values())
