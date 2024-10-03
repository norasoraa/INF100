def find_nth_occurence(search_string, character, n):
    teller = 0 #en variabel som teller hvor mange tilfeller du har funnet så langt
    for i in range(len(search_string)):
        if search_string[i] == character:
            teller += 1
        if teller == n:
            return i
    if teller != n:
        return -1

print(find_nth_occurence("abcabc", "a", 2))
