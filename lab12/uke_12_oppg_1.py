def filter_high_temperatures(path_input, path_output, threshold_temp):
    with open(path_input, "rt", encoding='utf-8') as f:
        file_as_string = f.read()
    file_as_dict = {}
    for line in file_as_string.splitlines():
        day, temperatur = line.split(" ")
        file_as_dict[day] =float(temperatur)
    path_output = ""
    for key in file_as_dict.keys():
        if file_as_dict[key] >= threshold_temp:
            path_output += key + " " + str(file_as_dict[key]) + "\n"
    with open("high_temps.txt", 'x') as f:
        f.write(path_output)

print("Tester filter_high_temperatures... ", end="")
filter_high_temperatures("temperatures.txt", "high_temps.txt", 23.5)
expected_result = """\
Monday 23.5
Wednesday 24.0
Thursday 23.9
Sunday 23.9
"""
with open("high_temps.txt", "rt", encoding='utf-8') as f: 
    actual_result = f.read()
assert(expected_result == actual_result)
print("OK")
