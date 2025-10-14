from main import get_days_from_today, get_numbers_ticket, normalise_phone_number, get_upcoming_birthdays

print(get_days_from_today("2025-01-01")) # should be 286 if today is 2025-10-14
print(get_days_from_today("2021-10-09")) # should be 1466 if today is 2025-10-14
print(get_numbers_ticket(1, 10, 3)) # should be a list of 3 random numbers between 1 and 10

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

for raw_number in raw_numbers:
    print(normalise_phone_number(raw_number))
    
users = [
    {"name": "John Doe", "birthday": "1985.10.15"},
    {"name": "Jane Smith", "birthday": "1990.10.18"}
]

print(get_upcoming_birthdays(users))