def num_pairwise_diff_gt10(a):
    teller = 0
    for i in range(len(a)-1):
        differanse = abs(a[i]-a[i+1])
        if differanse > 10:
            teller += 1
    return teller

a =[9, 3, 12, 0,- 3, 2, -9]  # Forskjellen er større: 12 -> 0 og 2 -> -9
print(num_pairwise_diff_gt10(a))
