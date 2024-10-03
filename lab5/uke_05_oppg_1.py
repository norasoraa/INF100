# Oppgave 1a
def remove_threes(a):
    while 3 in a:
        a.remove(3)

print()

# Oppgave 1b
def every_fourth(a):
    resultat_liste = []
    for i in range(len(a)):
        if i % 4 == 0:
            resultat_liste.append(a[i])
    return resultat_liste

a = list(range(10))
print(every_fourth(a))

print()

# Oppgave 1c
def halve_values(a):
    for i in range(len(a)):
        a[i]/=2

print()

# Oppgave 1d
def unique_values(a):
    resultat_liste = []
    for i in range(len(a)):
        if a[i] not in resultat_liste:
            resultat_liste.append(a[i])
    return resultat_liste

a = [1, 1, 2, 1, 3, 3, 3, 2]
print(unique_values(a))

print()

# Oppgave 1e
def add_list(a,b):
    for i in range(len(a)):
        a[i] = a[i] + b[i]