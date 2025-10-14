from datetime import datetime, timedelta
import random
import re

def get_days_from_today(date: str) -> int:
    today = datetime.today()
    date = datetime.strptime(date, "%Y-%m-%d")
    return (today - date).days

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    return random.sample(range(min, max), quantity)

def normalise_phone_number(phone: str) -> str:
    if phone.startswith("+"):
        phone = re.sub(r'[\D+]', '', phone)
    else:
        phone = re.sub(r'\D', '', phone)
    
    if phone.startswith("380") or phone.startswith("38"):
        phone = "+" + phone
    elif phone.startswith("0"):
        phone = "+38" + phone
    else:
        phone = "+380" + phone
    
    return phone

def get_upcoming_birthdays(users: list[dict[str, str]]) -> dict[str, str]:
    today = datetime.today()
    upcoming_birthdays = []
    for user in users:
        birthday = user["birthday"]
        
        user_birthday = datetime.strptime(birthday, "%Y.%m.%d")
        
        #adjust in case if birthday close to the current year
        closest_birthday = \
            user_birthday.replace(year=today.year) \
            if today - user_birthday.replace(year=today.year) <= timedelta(days=7)\
            else user_birthday.replace(year=today.year + 1)
        
        if (
            today - closest_birthday <= timedelta(days=7)
        ):
            if closest_birthday.weekday() >= 5:
                closest_birthday += timedelta(days=closest_birthday.weekday() - 4)
            upcoming_birthdays.append((user["name"], closest_birthday.strftime("%Y.%m.%d")))
    return {name: birthday for name, birthday in upcoming_birthdays}
        
        
        