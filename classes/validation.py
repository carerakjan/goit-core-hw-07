#Validation.for('birthday').validate()
import re


class ValidationError(Exception):
    pass

class Validation:
    validations = {}

    def __init__(self, name: str, pattern:str, error_message:str = '') -> None:
        self.name = name
        self.pattern = pattern
        self.error_message = error_message
        self.template = re.compile(pattern)

        Validation.validations[name] = self

    def validate(self, value: str):
        if not self.template.match(value):
            raise ValidationError(self.error_message or f'Does not math pattern "{self.pattern}"')
    
    @classmethod   
    def preset(cls, name:str):
        return cls.validations[name]

Validation('phone', r'^\d{10}$', "Invalid phone format. Use 10 digits")
Validation('birthday', r'^\d{2}\.\d{2}\.\d{4}$', "Invalid date format. Use DD.MM.YYYY")
