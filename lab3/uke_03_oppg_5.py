def split_line(x_lo, x_hi, n):
    # lengde på hvert linjestykke
    b = (x_hi - x_lo) / n
    x = 0
    for x in range(0, n):
        linje_start = x_lo + b * x
        linje_slutt = x_lo + b * (x+1)
        print(linje_start, linje_slutt)       

split_line(0.0, 1.0, 4)