def get_common_symbols(s1, s2):
    x = ""
    for i in s1:
        if (i in s2) and (i not in x):
            x += i
    return x

print(get_common_symbols("Hvor er du, Kari?", 
                                       "Her er jeg, Olav!"))