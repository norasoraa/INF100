def human_to_dog_years(x):
    if x <= 2:
        return x * 10.5
    else:
        return (x-2) * 4 + 21
print(human_to_dog_years(2))
print(human_to_dog_years(4))

def almost_equals(a, b):
    return abs(a - b) < 0.00000001

print(human_to_dog_years(1.5))
