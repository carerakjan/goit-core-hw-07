import re


class ValidationError(Exception):
    pass


class Validation:
    validations = {}

    def __init__(self, name: str, pattern: str, error_message: str = '') -> None:
        self.name = name
        self.pattern = pattern
        self.error_message = error_message
        self.template = re.compile(pattern)

        Validation.validations[name] = self

    def validate(self, value: str):
        if not self.template.match(value):
            raise ValidationError(self.error_message or f'Does not math pattern "{self.pattern}"')

    @classmethod
    def by_name(cls, name: str):
        try:
            return cls.validations[name]
        except KeyError:
            raise ValidationError(f'No such type of validation like "{name}"')


Validation('phone', r'^\d{10}$', "Invalid phone format. Use 10 digits")
Validation('birthday', r'^(0?[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[1,2])\.(19|20)\d{2}$',
           "Invalid date or date format. Use DD.MM.YYYY")
