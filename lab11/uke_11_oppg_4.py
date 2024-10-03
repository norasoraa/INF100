# Del A
def simplified_pig_latin(word):
    word = word.lower()
    if word[0] in "aeiou":
        return word + "hay"
    else:
        return (word[1:] + word[0] + "ay")

print(simplified_pig_latin("Hello"))


print()


# Del B
def sentence_to_simplified_pig_latin(sentence):
    setning = sentence.split()
    liste = []
    for i in range(len(setning)):
        word = setning[i]
        word = word.lower()
        if word[0] in "aeiou":
            liste.append(word + "hay")
        else:
            liste.append(word[1:] + word[0] + "ay")
    return " ".join(liste)

sentence = "My name is Sylvia Lavrans"
print(sentence_to_simplified_pig_latin(sentence))