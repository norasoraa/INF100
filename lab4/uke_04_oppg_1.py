def insert_at(source_string, index, insertion_string):
    første_del = source_string[0 : index]
    andre_del = source_string[index : len(source_string)]
    return (første_del + insertion_string + andre_del)

print(insert_at("abcd", 2, "XY"))