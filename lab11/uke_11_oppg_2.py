def read_file(path):
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()

def add_markers(filename):
    streng = read_file(filename)
    resultat = []
    for line in streng.splitlines():
        ny_linje = f">>>{line}<<<"
        resultat.append(ny_linje)
    resultat = "\n".join(resultat)
    return resultat + "\n"


print(add_markers("askeladden.txt"))