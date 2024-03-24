from classes import AddressBookRecord, AddressBook
from utils.decorators import input_error


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    new_contact = AddressBookRecord(name)
    new_contact.add_phone(phone)
    book.add_record(new_contact)

    return "Contact added."


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    contact = book.find(name)
    contact.edit_phone(old_phone, new_phone)

    return 'Contact updated.'


@input_error
def show_phone(args, book: AddressBook):
    return book.show_phones(args[0])


def show_all(book: AddressBook):
    return book


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    book.add_birthday(name, birthday)

    return 'Birthday added.'


@input_error
def show_birthday(args, book: AddressBook):
    return book.show_birthday(args[0])


def birthdays(book: AddressBook):
    return book.birthdays()
