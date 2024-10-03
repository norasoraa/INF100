def almost_equals(a, b):
   return abs(a - b) < 0.00000001

# Del A
def mean(a):
    total = 0
    for number in a:
        total += float(number)
    return total/(len(a))

assert(almost_equals(2.75, mean([2, 5, 3, 1])))

# Del B
def median(a):
    b = sorted(a)
    if len(b) % 2 != 0:
        x = int((len(b)-1)/2)
        return float(b[x])
    else:
        x1 = int(len(b)/2)
        x2 = int(len(b)/2 -1)
        return float(b[x1]+b[x2])/2

assert(almost_equals(5.0, median([4, 12, 3, 9, 5])))
assert(almost_equals(6.0, median([4, 12, 3, 9, 5, 7])))

# Del C
def mode(a):
    d = dict()
    for number in a:
        d[float(number)] = a.count(number)
    max_value = max(d.values())
    for key in d.keys():
        value = d[key]
        if max_value == value:
            return key

assert(almost_equals(4.0, mode([3, 4, 22, 7, 4, 15, 4, 7, 1])))

a = [3, 22, 7, 7, 7, 22.0, 3, 22.0] # Tricky case: både 22 og 22.0
assert(almost_equals(22.0, mode(a)))

# Sjekk at a ikke er mutert
for i, v in enumerate([3, 22, 7, 7, 7, 22.0, 3, 22.0]):
   assert(a[i] == v), f"Feil verdi: a[{i}]={a[i]}, men forventet {v}"
   assert(type(a[i]) == type(v)), f"Feil type: type(a[{i}])={type(a[i])}"

# Del D
def cmd_main():
    print("Regn ut statistiske gjennomsnitt for en liste.")
    print("Oppgi tallene du vil regne ut gjennomsnitt for, separert av mellomrom:")
    numbers = input()
    string = str(numbers)
    string = string.strip()
    a = string.split()
    print(len(a))
    print(f"Gjennomsnitt: {mean(a)}")
    print(f"Median: {median(a)}")
    print(f"Typetall: {mode(a)}")