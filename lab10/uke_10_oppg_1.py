# Del A
def at_least_two(word, c):
    for bokstav in word:
        if word.count(c) >= 2:
            return True
        else:
            return False
print(at_least_two('assessment', 's'))

print()

# Del B
def at_least_two_in_list(wordlist, c):
    resultat_liste = []
    for ord in range(len(wordlist)):
        word = wordlist[ord]
        for bokstav in word:
            if word.count(c) >= 2:
                resultat_liste.append(word)
                break
    return len(resultat_liste)
                
words = ['exam', 'christmas', 'assessment', 'test', 'paper', 'class']
print(at_least_two_in_list(words, 's'))

print()

# Del C
def read_file(path):
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()

def at_least_two_in_file(path, c):
    word_as_string = read_file(path)
    liste =[]
    for line in word_as_string.splitlines():
        liste.append(line)
    return at_least_two_in_list(liste, c)

print(at_least_two_in_file('wordlist.txt', 's'))
