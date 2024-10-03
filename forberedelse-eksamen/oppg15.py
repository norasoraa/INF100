def read_file(path):
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()
        
def file_as_list(path):
    file_as_string = read_file("No_ADM12.csv")
    file_as_list = []
    for line in file_as_string.splitlines():
        row = line.strip().split(";")
        file_as_list.append(row)
    return file_as_list           

def bare_fylke(path):
    liste = file_as_list("No_ADM12.csv")
    fylker = []
    for row in liste:
        if row[5] == "ADM1":
            fylker.append(row)
    return fylker

def bare_kommune(path):
    liste = file_as_list("No_ADM12.csv")
    kommuner = []
    for row in liste:
        if row[5] == "ADM2":
            kommuner.append(row)
    return kommuner

def print_county(county):
    alle_fylker = []
    alle_kommuner = []
    for row in bare_fylke("No_ADM12.csv"):
        alle_fylker.append(row[1])
    if county not in alle_fylker:
        return False
    for row in bare_fylke("No_ADM12.csv"):
        if row[1] == county:
            correct_county = row
            for i in bare_kommune("No_ADM12.csv"):
                if correct_county[7] == i[7]:
                    alle_kommuner.append(i)
    population = []
    latitude = []
    for row in alle_kommuner:
        population.append(int(row[9]))
        latitude.append(float(row[3]))
    max_population = max(population)
    max_latitude = max(latitude)
    min_population = min(population)
    min_latitude = min(latitude)
    for row in alle_kommuner:
        if str(max_population) in row:
            city_max_population = row[1]
        if str(min_population) in row:
            city_min_population = row[1]
        if str(max_latitude) in row:
            city_max_latitude = row[1]
        if str(min_latitude) in row:
            city_min_latitude = row[1]
    print("="*38)
    print(county)
    print("="*38)
    print(f'{city_max_population:25}{max_population:12}')
    print(f'{city_min_population:25}{min_population:12}')
    print(f'{city_max_latitude:20}{round(max_latitude, 1):6}')
    print(f'{city_min_latitude:20}{min_latitude:6}')
    print("="*38)

    if county in alle_fylker:
        return True

while True:
    print(f'Which county (q to quit)?', end=' ')
    county = input()
    if county == "q":
        print("Bye!")
        break
    elif print_county(county) == False:
        print('No matching county found. Try again.')
        continue