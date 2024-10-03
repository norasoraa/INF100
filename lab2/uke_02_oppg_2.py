def is_leap_year(year):
    x = year
    if x % 100 == 0 and x % 400 == 0:
        return True
    if x % 4 == 0 and x % 100 == 0:
        return False
    if x % 4 == 0:
        return True
    return False
print(is_leap_year(1996))
print(is_leap_year(1900))
print(is_leap_year(2000))