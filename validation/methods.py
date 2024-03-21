from validation.templates import phone_number_tmpl


def validate_phone_number(value, custom_error=None):
    matched = phone_number_tmpl.match(value)

    return bool(matched), custom_error or ValueError('The phone should consist of 10 digits.')
