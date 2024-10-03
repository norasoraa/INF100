def multiplication_table(n):
    x = 1
    for x in range(x, n + 1, 1):
        print(str(x) + ":", end=" ")
        for x in range (x, x * (n + 1), x):
            print(x, end=" ")
        print()

multiplication_table(5)