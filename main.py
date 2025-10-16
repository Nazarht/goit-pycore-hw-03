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
        raise ValueError("Minimum value must be greater than 0")
    if max > 1000:
        raise ValueError("Maximum value must be greater than 0")
    if quantity < min or quantity > max:
        raise ValueError("Quantity must be greater than minimum and less than maximum")
    
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
        
        #adjust in case if birthday close to the current year
        closest_birthday = \
            user_birthday.replace(year=today.year) \
            if today - user_birthday.replace(year=today.year) <= timedelta(days=7)\
            else user_birthday.replace(year=today.year + 1)
        
        if (
            closest_birthday - today <= timedelta(days=7)
        ):
            if closest_birthday.weekday() >= 5:
                closest_birthday += timedelta(days=closest_birthday.weekday() - 4)
            upcoming_birthdays.append((user["name"], closest_birthday.strftime("%Y.%m.%d")))
    return [{"name":name, "congratulation_date": birthday} for name, birthday in upcoming_birthdays]
        
        
        