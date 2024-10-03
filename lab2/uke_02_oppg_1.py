def find_longest_words(a,b,c):
    a_lengde = len(a)
    b_lengde = len(b)
    c_lengde = len(c)
    lengste_ord = max(a_lengde, b_lengde, c_lengde)
    if a_lengde == lengste_ord:
        print(a)
    if b_lengde == lengste_ord:
        print(b)
    if c_lengde == lengste_ord:
        print(c)
    elif (a_lengde, b_lengde) == lengste_ord:
        print(a,b)
    elif (a_lengde, c_lengde) == lengste_ord:
        print(a,c)
    elif (b_lengde, c_lengde) == lengste_ord:
        print(b,c)
    else:
        print(a,b,c)

find_longest_words("Game", "Action", "Champion")
find_longest_words("apple", "carrot", "ananas")
find_longest_words("Four", "Five", "Nine")