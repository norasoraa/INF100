def is_even_positive_int(x):
    if type(x) == int and x > 0 and x % 2 == 0:
        return True
    else:
        return False

print(is_even_positive_int(4))
