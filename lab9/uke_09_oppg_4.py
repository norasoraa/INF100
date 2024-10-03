# Del A
def shopping_list_to_dict(shopping_list_as_string):
    d = dict()
    for line in shopping_list_as_string.splitlines():
        num, food_name = line.split(" ")
        d[food_name] =int(num)
    return d

shopping_list_as_string = """\
2 brød
3 pizza
10 poteter
1 kaffe
1 ost
14 epler
"""
print(shopping_list_to_dict(shopping_list_as_string))

print()

# Del B
def shopping_list_file_to_dict(path):
    with open(path, "rt", encoding='utf-8') as f:
        return shopping_list_to_dict(f.read())

print(shopping_list_file_to_dict("handleliste.txt"))