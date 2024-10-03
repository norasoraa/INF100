def first_letter_last_word(path):
    with open(path, "rt", encoding='utf-8') as f:
        file_as_string = f.read()
    file_as_list = []
    for line in file_as_string.splitlines():
            line = line.strip().split(" ")
            file_as_list.append(line)
    result = ""
    length = len(file_as_list)
    for i in range(length):
        words = file_as_list[i][-1]
        words = list(words)
        result += words[0]
    return result
print(first_letter_last_word("askeladden.txt"))

print("Tester first_letter_last_word... ", end="")
assert("vlf" == first_letter_last_word("askeladden.txt"))
# Forklaring:
# Siste ord i første linje er 'vanns.'   Første bokstav i dette ordet er 'v'
# Siste ord i andre linje er 'landet.'   Første bokstav i dette ordet er 'l'
# Siste ord i tredje linje er 'fleste.'  Første bokstav i dette ordet er 'f'
print("OK")
