def find_first_longest_word(a,b,c):
    a_lengde = len(a)
    b_lengde = len(b)
    c_lengde = len(c)
    lengste_ord = max(a_lengde, b_lengde, c_lengde)
    if a_lengde == lengste_ord:
        print(a)
    elif b_lengde == lengste_ord:
        print(b)
    elif c_lengde == lengste_ord:
        print(c)
find_first_longest_word("Game", "Action", "Champion")
find_first_longest_word("apple", "carrot", "ananas")
find_first_longest_word("Four", "Five", "Nine")

