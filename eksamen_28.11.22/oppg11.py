def count_a(s):
    for c in range(len(s)):
        count = 0
        if c == "a":
            count += 1
        return count

print(count_a("heisann"))


def count_a(s):
    count = 0
    for c in range(len(s)):
        if s[c] == "a":
            count += 1
    return count

print(count_a("abelana"))