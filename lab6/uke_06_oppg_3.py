import copy

def median(a):
    b = copy.copy(a)
    b.sort()
    if len(b) % 2 != 0:
        x = int((len(b)-1)/2)
        return b[x]
    else:
        x1 = int(len(b)/2)
        x2 = int(len(b)/2 -1)
        return (b[x1]+b[x2])/2

a = [-10, 100, 8, 7, 2]
print(median(a))
