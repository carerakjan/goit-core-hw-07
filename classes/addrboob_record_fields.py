from classes.validation import Validation
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        Validation.preset('phone').validate(value)
        super().__init__(value)



class Birthday(Field):
    def __init__(self, value):
        Validation.preset('birthday').validate(value)
        super().__init__(datetime.strptime(value, '%d.%m.%Y'))

    def __str__(self):
       return self.value.strftime('%Y.%m.%d')
