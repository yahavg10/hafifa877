from datetime import datetime, timedelta

def days_until_birthday(birthday):
    today = datetime.now()
    next_birthday = datetime(today.year, birthday.month, birthday.day)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birthday.month, birthday.day)
    return (next_birthday - today).days

my_birthday = datetime(2024, 5, 10)
days_left = days_until_birthday(my_birthday)
print(f"There are {days_left} days left until my next birthday.")