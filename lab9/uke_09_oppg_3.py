def rotate(grid):
    resultat_liste = []
    col = 0
    for col in range(len(grid[0])):
        liste = []
        for row in range(len(grid)):
            liste.append(grid[row][col])
        resultat_liste.append(liste)
    return resultat_liste
a = [
    [1, 4],
    [2, 5],
    [3, 6],
]
print(rotate(a))

