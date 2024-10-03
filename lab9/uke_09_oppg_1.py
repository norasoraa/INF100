def will_work(city, salary):
    if city == "Bergen" and salary >= 400000:
        return True
    elif city == "Bodø" and salary >= 900000:
        return True
    elif city == "Verdensrommet":
        return True
    elif salary >= 600000 and city != "Bodø":
        return True
    else:
        return False


print(will_work('Kristiansand', 590_000))
