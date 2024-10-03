def has_consecutive_elements(a):
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return True
    return False
print(has_consecutive_elements([1, 5, 5, 4]))
