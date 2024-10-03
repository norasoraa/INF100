# oppgave 6a
def g(x):
    return (1/8) * x**2 - 2 * x + 10
    
print(g(8.0))

def almost_equals(a, b):
    return abs(a - b) < 0.0000001

print()

# oppgave 6b
def approx_area_under_g(x_lo, x_hi):
    # i er arealet
    i = 0
    for x in range(x_lo, x_hi):
        i += g(x)
    return i

print(approx_area_under_g(5, 6))

print()

# oppgave 6c
def riemann_sum_g(x_lo, x_hi, n):
    # bredde på hvert trappetrinn
    areal_totalt = 0
    b = ((x_hi - x_lo) / n)
    for x_i in range(0,n):
        x_i = x_lo + b * x_i
        a_søyle = b * g(x_i)
        areal_totalt += a_søyle
    return areal_totalt

print(riemann_sum_g(4,6,2))

print()

# oppgave 6d
def riemann_sum(f, x_lo, x_hi, n):
    areal = 0
    b = ((x_hi - x_lo) / n)
    for x_i in range(0,n):
        x_i = x_lo + b * x_i
        a = b * f(x_i) #bytter ut g(x_i) fra forrige oppgave med f
        areal += a
    return areal
    