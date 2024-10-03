def is_legal_triangle(x, y, z):
    if (type(x) and type(y) and type(z)) != int:
        return False
    if x >= y + z or y >= x + z or z >= x + y:
        return False
    else:
        return True

print(is_legal_triangle(3,4,5))
