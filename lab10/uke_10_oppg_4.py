def read_file(path):
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()

def people_with_age(path, age):
    s = set()
    streng = read_file(path)
    name_age = streng.splitlines()
    for i in range(len(name_age)):
        name, number = name_age[i].split(" ")
        if int(number) == age:
            s.add(name)
    return s

print(people_with_age('namesages.txt', 18))