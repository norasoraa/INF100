def read_file(path):
    with open("NO_ADM12.csv", "rt", encoding='utf-8') as f:
        file_as_string = f.read()
        file_as_list = []
        for line in file_as_string.splitlines():
            row = line.strip().split(";")
            file_as_list.append(row)
    return file_as_list

list = read_file("NO_ADM12.csv")
municipalities = []
counties = {}

for row in list[1:]:
    name = row[1]
    latitude = float(row[3])
    longitude = float(row[4])
    feature_code = row[5]
    admin1_code = row[7]
    population = int(row[9])

    if feature_code == "ADM1":
        counties[admin1_code] = name
    elif feature_code == "ADM2":
        municipalities.append({
            "name": name, 
            "county_code": admin1_code, 
            "latitude": latitude, 
            "longitude": longitude, 
            "population": population})

def municipalities_in_county(county, municipalities, counties):
    result = []
    for municipality in municipalities:
        correct_county_code = municipality["county_code"]
        correct_county_name = counties[correct_county_code]
        
        if county == correct_county_name:
            result.append(municipality)
    return result

def largest_municipality(municipalities):
    largest = 0
    largest_mun = {}
    for municipality in municipalities:
        if municipality["population"] > largest:
            largest = municipality["population"]
            largest_mun = municipality
    return largest_mun

def smallest_municipality(municipalities):
    smallest = 
    smallest_mun = {}
    for municipality in municipalities:
        if municipality["population"] < smallest:
            pass
