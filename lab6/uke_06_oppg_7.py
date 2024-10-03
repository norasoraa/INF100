def read_file(path):
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()

def check_conditions(row):
    kartleggingsprøve = False
    quiz_teller = row[13:17].count("B")
    første_laber_teller = row[2:7].count("B")
    siste_laber_teller = row[8:13].count("B")
    if row[1] == "B":
        kartleggingsprøve = not kartleggingsprøve
    if quiz_teller != 4:
        return False
    if siste_laber_teller >= 3:
        if kartleggingsprøve or første_laber_teller + siste_laber_teller >= 6:
            return True

def students_who_passed(path):
    path_as_string = read_file(path)
    passed = []
    for line in path_as_string.splitlines():
        row = line.strip().split(";")
        if check_conditions(row) == True:
            passed.append(row[0])
    return passed
        
print(students_who_passed("course_data.csv"))