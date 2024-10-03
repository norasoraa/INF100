def mix(s1,s2):
    x = ""
    for i in range(0, max(len(s1), len(s2))):
        if i < len(s1):
            x += s1[i]
        if i < len(s2):
            x += s2[i]
    return x

print(mix("abc", "123"))

