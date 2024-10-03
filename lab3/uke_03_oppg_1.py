def multiples_of_seven_up_to(n):
    x = 1
    while x < n:
        if x % 7 == 0:
            print(x)
        x += 1

multiples_of_seven_up_to(49)