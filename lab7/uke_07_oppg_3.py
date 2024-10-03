def sum_col(grid):
    col_2 = []
    row = 0
    for col in range(len(grid[row])):
        col_1 = []
        col_2.append(col_1)
        for row in range(len(grid)): 
            tall = grid[row][col]
            col_1.append(tall)
            row += 1
    sum_col = []
    for row in range(len(col_2)):
        row_1 = col_2[row]
        sum = 0
        for i in range(len(row_1)):
            sum += row_1[i]
        sum_col.append(sum)
    for i in range(len(sum_col)-1):
        if sum_col[i] == sum_col[i+1]:
            i += 1
        else:
            return False
    return True
  

def sum_row(grid):
    sum_row = []
    for row in range(len(grid)):
        row_1 = grid[row]
        sum = 0
        for i in range(len(row_1)):
            sum += row_1[i]
        sum_row.append(sum)
    for i in range(len(sum_row)-1):
        if sum_row[i] == sum_row[i+1]:
            i += 1
        else:
            return False
    return True


def all_rows_and_cols_equal_sum(grid):
    if sum_col(grid) and sum_row(grid) == True:
        return True
    else:
        return False


print(all_rows_and_cols_equal_sum([
        [1, 2, 3, 4], # alle rader og kolonner summerer til 10
        [2, 3, 4, 1],
        [3, 4, 1, 2],
        [4, 1, 2, 3],
    ]))