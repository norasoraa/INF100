# Del A
def compress(raw_binary):
    a = list(raw_binary)
    resultat = []
    teller = 1
    if a[0] == "1":
        resultat.append("0")
    for i in range(len(raw_binary)-1):
        if a[i] == a[i+1]:
            teller += 1
        if a[i] != a[i+1]:
            resultat.append(str(teller))
            teller = 1
    resultat.append(str(teller))

    return (" ".join(resultat))

print(compress("0011100001111"))


# Del B
def decompress(compressed_binary):
    a = "".join(compressed_binary.split())
    resultat = ""
    for i in range(len(a)):    
        teller = a[i]     
        if i % 2 == 0:
            resultat += (int(teller) * "0")
        if i % 2 != 0:
            resultat += (int(teller) * "1")
    return resultat

print(decompress("0 2 1 8 1"))
