# oppgave 4a
def good_style(source_code):
    for line in source_code.splitlines():
        teller = 0
        for i in line:
            teller += 1
            if teller >= 80:
                return False
    return True

print(good_style((("x" * 79) + "\n") * 20))
print(good_style("x" * 81))

print()

# oppgave 4b
def good_style_from_file(filename):
    with open(filename, "rt") as f:
        innhold_i_fil = f.read()
        if good_style(innhold_i_fil) == True:
            return True
        else:
            return False

print(good_style_from_file("test_file1.py"))
print(good_style_from_file("test_file2.py"))
print(good_style_from_file("uke_04_oppg_4.py"))