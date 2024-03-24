from classes import AddressBookRecord, AddressBook
from utils.decorators import input_error


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = AddressBookRecord(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        return 'Contact not found.'
    phone = record.find_phone(old_phone)
    if phone is None:
        return 'No number to change.'
    record.edit_phone(old_phone, new_phone)
    return 'Contact updated.'


@input_error
def show_phone(args, book: AddressBook):
    record = book.find(args[0])
    if record is None:
        return 'Contact not found.'
    return record.stringify_phones()


def show_all(book: AddressBook):
    return book or 'No contacts yet.'


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    message = 'Birthday added.'
    if record is None:
        return 'Contact not found.'
    if record.birthday:
        message = 'Birthday updated.'
    record.add_birthday(birthday)
    return message


@input_error
def show_birthday(args, book: AddressBook):
    record = book.find(args[0])
    if record is None:
        return 'Contact not found.'
    if record.birthday is None:
        return 'Contact has no birthday yet.'
    return record.birthday


def birthdays(book: AddressBook):
    if not book:
        return 'No contacts yet.'
    congratulation_list = book.get_congratulation_list()
    if not congratulation_list:
        return 'No one to congratulate.'
    return '\n'.join(
        (f"Contact name: {item['name']}, "
         f"congratulate: {item['congratulation_date']}") for item in congratulation_list
    )
