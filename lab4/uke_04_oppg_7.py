from uke_04_oppg_3 import find_nth_occurence

# Del A
def get_impact(line):
    andre = find_nth_occurence(line, ";",2)
    tredje = find_nth_occurence(line, ";",3)
    impact = float(line[andre+1:tredje])
    return impact
    
print(get_impact("nc72666881;California;1.43;2016-07-27 00:19:43"))

print()

# Del B
def filter_earthquakes(earthquake_csv_string, threshold):
    csv_to_list = earthquake_csv_string.splitlines()
    result = [csv_to_list[0]]
    each_earthquake = csv_to_list[1:]
    for i in range(len(each_earthquake)):
        impact = get_impact(each_earthquake[i])
        if impact >= threshold:
            result.append(each_earthquake[i])
    result = "\n".join(result)
    return "\n" + result + "\n"


print(filter_earthquakes("""\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
nc72666891;California;0.06;2016-07-27 00:31:37
""", 5.0))

print("Tester filter_earthquakes... ", end="")
assert("""\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
""" == filter_earthquakes("""\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
nc72666891;California;0.06;2016-07-27 00:31:37
""", 1.1))
assert("""\
id;location;impact;time
us20006i0y;Burma;4.9;2016-07-27 00:20:28
""" == filter_earthquakes("""\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
nc72666891;California;0.06;2016-07-27 00:31:37
""", 3.0))
assert("""\
id;location;impact;time
""" == filter_earthquakes("""\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
nc72666891;California;0.06;2016-07-27 00:31:37
""", 5.0))
print("OK")
