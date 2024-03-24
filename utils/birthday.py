import calendar
from datetime import datetime, timedelta


def get_birthday_this_year(user):
    birthday = datetime.strptime(user['birthday'], '%Y.%m.%d')
    today = datetime.today()

    if calendar.isleap(birthday.year) and \
            not calendar.isleap(today.year) and \
            user['birthday'].find('02.29') > 0:
        return datetime(today.year, month=3, day=1).date()

    return datetime(today.year, month=birthday.month, day=birthday.day).date()


def add_congratulation_date(user):
    user_copy = user.copy()
    user_birthday_this_year = get_birthday_this_year(user)
    today = datetime.today().date()

    if user_birthday_this_year < today or \
            (user_birthday_this_year - today).days > 7:
        return

    congratulation_date = user_birthday_this_year
    weekday = user_birthday_this_year.weekday()

    if weekday > 4:
        next_monday = user_birthday_this_year + timedelta(7 - weekday)
        congratulation_date = next_monday

    del user_copy['birthday']

    user_copy['congratulation_date'] = congratulation_date.strftime('%Y.%m.%d')

    return user_copy


def get_upcoming_birthdays(users):
    return [u for u in [add_congratulation_date(user) for user in users] if u]

# users = [
#     {"name": "John Doe", "birthday": "1985.02.24"},
#     {"name": "Jane Smith", "birthday": "1992.02.29"}
# ]

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("The birthdays on this week:", upcoming_birthdays)
