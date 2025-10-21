from main import get_days_from_today, get_numbers_ticket, normalize_phone, get_upcoming_birthdays

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
    print(normalize_phone(raw_number))
    
users = [
   {'name': 'Before Before Yesterday', 'birthday': '1986.10.18'},
   {'name': 'Before Yesterday', 'birthday': '2007.10.19'},
   {'name': 'Yesterday', 'birthday': '1976.10.20'},
   {'name': 'Today', 'birthday': '1950.10.21'},
   {'name': 'Tomorrow', 'birthday': '1961.10.22'},
   {'name': 'After Tomorrow', 'birthday': '1973.10.23'},
   {'name': 'After After Tomorrow', 'birthday': '1967.10.24'},
   {'name': 'In Four Days', 'birthday': '1970.10.25'},
   {'name': 'In Five Days', 'birthday': '1959.10.26'},
   {'name': 'In Six Days', 'birthday': '1954.10.27'},
   {'name': 'In Seven Days', 'birthday': '1979.10.28'},
   {'name': 'In Eight Days', 'birthday': '1984.10.29'},
]

print(get_upcoming_birthdays(users))