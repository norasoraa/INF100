# Del A
def can_be_made_of_letters(word, letters):
    for bokstav in word:
        if word.count(bokstav) > letters.count(bokstav):
            return False
    return True
print(can_be_made_of_letters("emoji", "abcdefghijklmno"))

print()

# Del B
def possible_words(wordlist, letters):
    resultat_liste = []
    for i in range(len(wordlist)):
        for bokstav in wordlist[i]:
            if wordlist[i] in resultat_liste:
                break
            if wordlist[i].count(bokstav) > letters.count(bokstav):
                break
        else:
            resultat_liste.append(wordlist[i])
    return resultat_liste

hundsk =["tur", "mat", "kos", "hent", "sitt", "dekk", "voff"]
print(possible_words(hundsk, "fikmopsttuv"))

print()

# Del C
def read_file(path):
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()

def possible_words_from_file(path, letters):
    word_as_string = read_file(path)
    liste =[]
    for line in word_as_string.splitlines():
        liste.append(line)
    return possible_words(liste, letters)

print(possible_words_from_file("nsf2022.txt", "hund"))
