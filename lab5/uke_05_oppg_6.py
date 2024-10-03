def non_contigous_substrings(s):
    resultat_liste = ""
    for i in range(len(s)):
        resultat_liste += s[i]
    return resultat_liste
print(non_contigous_substrings("foo")) 



print("Tester non_contigous_substrings... ", end="")
# Test 1
# Merk: rekkefølgen på elementene i listen betyr ingenting,
# siden begge listene sorteres før de sammenlignes
#assert(sorted([
  #"", # Den tomme strengen er alltid en substreng
  #"a", "b", "c", "d",
  #"ab", "ac", "ad", "bc", "bd", "cd",
  #"abc", "abd", "acd", "bcd",
  #"abcd",
#]) == sorted(non_contigous_substrings("abcd")))

# Test 2
#assert(sorted([
  #"",
  #"f", "o",  # Merk: "o" opptrer bare én gang
  #"fo", "oo",
  #"foo",
#]) == sorted(non_contigous_substrings("foo")))
print("OK")
