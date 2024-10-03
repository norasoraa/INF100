def alternate_sign_sum(a):
    x = 0
    for i in range(len(a)):
        if i % 2 == 0:
            x += a[i]
        else:
            x -= a[i]
        
    return x

print(alternate_sign_sum([10, 20, 30, 40, 50]))
