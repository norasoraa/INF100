from datetime import datetime, timedelta

def is_friday_13th(date):
    day_name = datetime.date(date).weekday()
    day_date = date.day
    if day_name == 4 and day_date == 13:
        return True
    else: 
        return False

def first_friday_13th_after(date):
    is_friday_13th(date)
    while is_friday_13th != True:
        date += timedelta(days = 1)
        if is_friday_13th(date) == True:
            return date

result = first_friday_13th_after(datetime(2022, 10, 24))
print(result.year, result.month, result.day)