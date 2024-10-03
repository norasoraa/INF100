def word_includes_all(single_word, must_include):
    for letter in must_include:
        if letter not in single_word:
            return False
    return True

def word_excludes_all(single_word, must_exclude):
    for letter in must_exclude:
        if letter in single_word:
            return False
    return True

def words_that_include(words, must_include):
    liste = []
    for word in words:
        if word_includes_all(word, must_include):
            liste.append(word)
    return liste

def words_that_exclude(words, must_exclude):
    liste = []
    for word in words:
        if word_excludes_all(word, must_exclude):
            liste.append(word)
    return liste

def filter_words(words, must_include, must_exclude):
    result = words_that_include(words, must_include)
    return words_that_exclude(result, must_exclude)

word_list = ["kattepus", "hundevofs", "kosebamse", "kanintuss", "slangesvin"]
must_include = {"a", "s"}
must_exclude = {"m", "v"}

print(filter_words(word_list, must_include,must_exclude))