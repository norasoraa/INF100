import csv

def read_csv_file(path, encoding="utf-8", **kwargs):
    r''' Reads a csv file from the provided path, and returns its
    content as a 2D list. The default encoding is utf-8, the default
    column delimitier is comma and the default quote character is the
    double quote character ("), though this can be overridden with
    named parameters "delimiter" and "quotechar".'''
    with open(path, "rt", encoding=encoding, newline='') as f:
        return list(csv.reader(f, **kwargs))

adm_table = read_csv_file("NO_ADM12.csv", delimiter=";")

# Alternativ uten å bruke csv-modulen:
# with open("NO_ADM12.csv", "rt", encoding='utf-8') as f:
#     adm_table = [line.strip().split(";") for line in f.readlines()]

# Liste med oppslagsverk, ett oppslagsverk per kommune
municipalities = []
# Oppslagsverk, nøkkelen er fylkeskode, verdiene er navn på fylket
counties = {}

for row in adm_table[1:]:
    name = row[1]
    lat = float(row[3])
    lon = float(row[4])
    county_code = row[7]
    population = int(row[9])

    if row[5] == "ADM1":
        # Fylke
        counties[county_code] = name
    elif row[5] == "ADM2":
        # Kommune
        municipalities.append({
            "name": name,
            "county_code": county_code,
            "lat": lat,
            "lon": lon,
            "population": population,
        })

def get_municipalities_in(county_name, municipalities, counties):
    result = []
    for mun in municipalities:
        this_county_code = mun["county_code"]
        this_county_name = counties[this_county_code]

        if county_name == this_county_name:
        # Alternativ if-setning som ikke krever at man staver nøyaktig:
        # if this_county_name.lower().startswith(county_name.lower()):
            result.append(mun)
    return result

def get_largest(munlist):
    largest_size = -1
    largest = {}
    for mun in munlist:
        if mun["population"] > largest_size:
            largest_size = mun["population"]
            largest = mun
    return largest

def get_smallest(munlist):
    smallest_size = float("inf")
    smallest = {}
    for mun in munlist:
        if mun["population"] < smallest_size:
            smallest_size = mun["population"]
            smallest = mun
    return smallest

def get_northernmost(munlist):
    largest_lat = -float("inf")
    largest = {}
    for mun in munlist:
        if mun["lat"] > largest_lat:
            largest_lat = mun["lat"]
            largest = mun
    return largest

def get_southernmost(munlist):
    smallest_lat = float("inf")
    smallest = {}
    for mun in munlist:
        if mun["lat"] < smallest_lat:
            smallest_lat = mun["lat"]
            smallest = mun
    return smallest

def print_county(county_name, municipalities, counties):
    munlist = get_municipalities_in(county_name, municipalities, counties)
    if len(munlist) == 0:
        return False

    print("="*38)
    print(county_name)
    print("="*38)
    bigcity = get_largest(munlist)
    print(f'{bigcity["name"]:25} {bigcity["population"]:12}')
    smallcity = get_smallest(munlist)
    print(f'{smallcity["name"]:25} {smallcity["population"]:12}')
    northern = get_northernmost(munlist)
    print(f'{northern["name"]:20} {round(northern["lat"], 1):6}˚N '
        + f'{round(northern["lon"], 1):6}˚Ø')
    southern = get_southernmost(munlist)
    print(f'{southern["name"]:20} {round(southern["lat"], 1):6}˚N '
        + f'{round(southern["lon"], 1):6}˚Ø')
    print("="*38)
    return True

while True:
    print("Which county (q to quit)?", end=" ")
    county_name = input()
    if county_name == "q":
        break
    if not print_county(county_name, municipalities, counties):
        print("No matching county found. Try again.")
