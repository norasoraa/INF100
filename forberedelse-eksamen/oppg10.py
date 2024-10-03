start_pris = 100
ny_pris = start_pris * 1.5
ny_pris = ny_pris * 0.5
ny_pris = ny_pris * 1.5
ny_pris = ny_pris * 0.5
ny_pris = ny_pris * 1.5
ny_pris = ny_pris * 0.5
print(ny_pris)


# Riktig måte å skrive på
x = 100
for i in range(3):
    x = x * 1.5
    x = x * 0.5
print(x)