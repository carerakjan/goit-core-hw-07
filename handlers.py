from decorators import input_error, parse_error
from classes import Record, AddressBook


@parse_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    new_contact = Record(name)
    new_contact.add_phone(phone)
    book.add_record(new_contact)
    return "Contact added."


@input_error
# TODO: ???
def change_contact(args, book: AddressBook):
    name, phone = args
    contact = book.find(name)
    # contact.e
    return 'Contact updated.'


@input_error
def show_phone(args, book: AddressBook):
    return book.find(args[0]).phones


def show_all(book: AddressBook):
    return book

@input_error
def add_birthday(args, book: AddressBook):
    book.add_birthday(*args)


@input_error
def show_birthday(args, book: AddressBook):
    return book.find(args[0]).birthday

@input_error
def birthdays(args, book: AddressBook):
    return book.birthdays()