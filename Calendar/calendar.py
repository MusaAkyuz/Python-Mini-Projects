import keyboard
import calendar
import datetime

year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day

print("\tToday Calendar\t\n")
print(calendar.month(year, month))
