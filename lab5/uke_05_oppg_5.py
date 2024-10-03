def complement(seq):
    resultat = ""
    for i in seq:
        if i == "A":
            resultat += "T"
        if i == "C":
            resultat += "G"
        if i == "G":
            resultat += "C"
        if i == "T":
            resultat += "A"
    
    return(resultat[::-1])

print(complement("ATAGCAGT"))
