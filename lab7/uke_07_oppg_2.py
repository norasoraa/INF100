# Del A
def remove_row(grid, row):
    grid.pop(row)


# Del B
import copy
def row_removed(grid, row):
    kopi_grid = copy.deepcopy(grid)
    ny_liste = kopi_grid[:row] + kopi_grid[row+1:]
    return ny_liste

grid = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]
    ]
print(row_removed(grid, 1))

print()

# Del C
def remove_col(grid, col):
    rows = len(grid)
    for row in range(rows):
        grid[row].pop(col)

print()

# Del D
#import copy
def col_removed(grid, col):
    result = []
    kopi_grid = copy.deepcopy(grid)
    rows = len(kopi_grid)
    for row in range(rows):
        rad_grid = kopi_grid[row]
        ny_liste = rad_grid[:col] + rad_grid[col+1:]
        result.append(ny_liste)
    return result

grid = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]
    ]
print(col_removed(grid, 0))