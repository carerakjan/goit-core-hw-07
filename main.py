from assistant import run_assistant
from classes import AddressBook


def main():
    book = AddressBook()

    run_assistant(book)


if __name__ == "__main__":
    main()
