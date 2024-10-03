def smallest_absolute_difference(a):
    list_difference = []
    list_sorted = sorted(a)
    for i in range(len(list_sorted)-1):
        list_difference.append(abs(list_sorted[i]-list_sorted[i+1]))
    return min(list_difference)
    
a = [67, 19, 40, -5, 1]
print(smallest_absolute_difference(a))
