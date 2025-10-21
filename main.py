from datetime import datetime, timedelta
import random
import re

def get_days_from_today(date: str) -> int:
    
    today = datetime.today()
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        return (today - date).days
    except ValueError:
        return "Invalid date format"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1:
        return []
    if max > 1000:
        return []
    if quantity > max - min:
        return []
    return sorted(random.sample(range(min, max), quantity))

def normalize_phone(phone: str) -> str:
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
        
        closest_birthday = \
            user_birthday.replace(year=today.year) \
            if today - user_birthday.replace(year=today.year) <= timedelta(days=7) and user_birthday.replace(year=today.year) > today\
            else user_birthday.replace(year=today.year + 1)
        
        if (
            closest_birthday - today <= timedelta(days=7)
        ):
            if closest_birthday.weekday() >= 5:
                closest_birthday += timedelta(days=(2 if closest_birthday.weekday() == 5 else 1))
            upcoming_birthdays.append((user["name"], closest_birthday.strftime("%Y.%m.%d")))
    return [{"name":name, "congratulation_date": birthday} for name, birthday in upcoming_birthdays]
        
        
        