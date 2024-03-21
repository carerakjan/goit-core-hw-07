import re

phone_number_tmpl = re.compile(r'^\d{10}$')

birthday_tmpl = re.compile(f'^\d{2}\.\d{2}\.\d{4}$')