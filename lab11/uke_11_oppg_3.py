# Del A
def read_file(path):
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()

def sub_course_positions(path):
    forward = 0
    depth = 0
    liste = []
    streng = read_file(path)
    for line in streng.splitlines():
        line = line.split(" ")
        liste.append(line)
    for i in range(len(liste)):
        if liste[i][0] == "forward":
            forward += int(liste[i][1])
        if liste[i][0] == "down":
            depth += int(liste[i][1])
        if liste[i][0] == "up":
            depth -= int(liste[i][1])
    d = dict()
    d["forward"] = forward
    d["depth"] = depth
    return d
    
print(sub_course_positions("sub-path-sample.txt"))


print()


# Del B
def sub_course(path):
    d = sub_course_positions(path)
    sum = 1
    for value in d.values():
        sum *= value
    return sum

print(sub_course("sub-path-sample.txt"))