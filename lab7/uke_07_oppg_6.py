first_line = input()
rows, cols = first_line.split(" ")
rows = int(rows)
cols = int(cols)

tt = []
for i in range(rows):
    line = input()
    splitted_line = line.split(" ")
    splitted_line_of_ints = []
    for str_item in splitted_line:
        num_item = int(str_item)
        splitted_line_of_ints.append(num_item) # eller kan bruke += i stedet for append
    tt.append(splitted_line_of_ints)

tf = []
for i in range(rows):
    tf.append([0] * cols)

# Regn ut første kolonne
for row in range(rows):
    if row != 0:
        tf[row][0] = tf[row-1][0] + tt[row][0]
    else:
        tf[row][0] = tt[row][0]

# Regn ut første rad
for col in range(1,cols):
    tf[0][col] = tf[0][col-1] + tt[0][col]

# Regn ut resten
for row in range(1,rows):
    for col in range(1,cols):
        tf[row][col] = max(tf[row-1][col], tf[row][col-1]) + tt[row][col]

# Skriv ut siste kolonne, med mellomrom mellom
for row in range(rows):
    x = tf[row][-1]
    print(x, end=" ")