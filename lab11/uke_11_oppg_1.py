def dot_product(a, b):
    sum = 0
    for i in range(len(a)):
        sum += a[i]*b[i]
    return sum

print(dot_product([1, 2, 3], [4, 5, 6]))