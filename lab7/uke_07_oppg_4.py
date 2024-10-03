def find_words_in_character_grid(char_grid, words):
    possible_words = []
    for col in range(len(char_grid[0])):
        word = ""
        for row in range(len(char_grid)):
            word += char_grid[row][col]
        possible_words.append(word)
    
    for row in range(len(char_grid)):
        word = ""
        for col in range(len(char_grid[0])):
            word += char_grid[row][col]
        possible_words.append(word)

    result = []
    for possible_word in possible_words:
        for word in words:
            if word in possible_word:
                result.append(word)

    return result


glossary = ["dikt", "hus", "lese", "by", "elev",
            "smart", "helt", "mål", "yr", "lære"]
char_grid= [
        ['d','s','h','s','s','y'],
        ['l','æ','r','e','s','å'],
        ['k','a','l','a','m','e'],
        ['t','h','e','r','a','q'],
        ['e','t','s','t','r','z'],
        ['e','t','e','r','t','p'],
        ['e','m','å','l','v','w'],
    ]

print(find_words_in_character_grid(char_grid, glossary))