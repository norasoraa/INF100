def sort_by_sign(a):
    liste_1 = []
    liste_2 = []
    liste_3 = []
    for i in range(len(a)):
        if a[i] < 0:
            liste_1.append(a[i])
        if a[i] == 0:
            liste_2.append(a[i])
        if a[i] > 0:
            liste_3.append(a[i])
    return liste_1 + liste_2 + liste_3

a = [3, -4, 1, 0, -1, 0, -2]
print(sort_by_sign(a))