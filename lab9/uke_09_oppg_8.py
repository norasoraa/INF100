def word_comparison(word_1, word_2):
    d = dict()
    exist_in_both = set()
    only_in_first = set()
    only_in_second = set()
    for letter in word_1:
        if letter in word_2:
            exist_in_both.add(letter)
        if letter not in word_2:
            only_in_first.add(letter)
    for letter in word_2:
        if letter not in word_1:
            only_in_second.add(letter)

    d["In common"] = exist_in_both
    d["Unique to first word"] = only_in_first
    d["Unique to second word"] = only_in_second
    return d


print(word_comparison("computer", "science"))
