a = [1, 2.2, "3", "a"]
b = "foo"
c = 42
d = { "a":"b", "b":"c" }
e = True


print(type(a[0]))
print(type(c < 42))

print(type(b + "a[0]"))
#error

#error
print(type(e))

a = 0
b = "foo"
c = "bar"
print((not a) and b)

d = {
    42 : 0,
    '42' : 'bar',
    'foo' : 42,
    95 : 'foo',
    'bar' : 95,
}
 
print(d[95] == 'foo')
print('bar' == d['42'])
print(0 in d.values())
print("foo" == d[d['bar']])

a = [[1, 2, 3], "foo", [42], 95]

print(42 in a[2])

x = 'foo'
if len(x) <= 3:
    print("A")
elif len(x) == 3:
    print("B")
elif not False:
    print("C")
if not True:
    print("D")

a = [['foo', 'bar'],'a']
b = [a[0], 'b']

a = [[95,24], [42],100]
print(a[-3])