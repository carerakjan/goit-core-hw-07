from classes.addrboob_record_fields import Name, Phone, Birthday


class AddressBookRecord:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        phone = Phone(phone_number)

        if not self.find_phone(phone_number):
            self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [item for item in self.phones if item.value != phone_number]

    def edit_phone(self, old_number, new_number):
        new_phone = Phone(new_number)
        found_phone = self.find_phone(old_number)

        if not found_phone:
            raise Exception('No number to change')

        found_phone.value = new_phone.value

    def find_phone(self, phone_number):
        return next((item for item in self.phones if item.value == phone_number), None)

    def stringify_phones(self):
        return '; '.join(p.value for p in self.phones)

    def add_birthday(self, birthday):
        if self.birthday:
            raise Exception('Birthday already specified')

        self.birthday = Birthday(birthday)

    def __str__(self):
        parts = [p for p in [
            f"Contact name: {self.name.value}",
            f"birthday: {self.birthday}" if self.birthday else '',
            f"phones: {self.stringify_phones()}"
        ]]
        return ', '.join(parts)
