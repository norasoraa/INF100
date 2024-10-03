def read_and_sort():
    sortert_liste = []
    while 0 not in sortert_liste:
        sortert_liste.append(int(input()))
    sortert_liste.pop()
    sortert_liste.sort()
    
    for i in range(len(sortert_liste)):
        print(sortert_liste[i])

read_and_sort()
