a = [1.1, 11] 
b = "11"
c = 11
d = b * a[1]

print(type(c == "11"))
print(type(f"{a}"))
print(type(b*c))
print(type(a[1]))
print(type(d))
print(type(len(a)))
#error
print(type([d]))
#error
print(type(c*a))