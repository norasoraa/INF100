# Del A
def key_value_getter(d):
    print("Dictionary keys:")
    for key in d:
        print(key)
    print()
    
    print("Dictionary values:")
    for value in d.values():
        print(value)
    print()

    print("Dictionary keys/value:")
    for key in d:
        value = d[key]
        print(key, value)

key_value_getter({
  "monday": 0,
  "tuesday": 0.7,
  "wednesday": 0,
  "thursday": 4.7,
  "friday": 10
})

print()

# Del B
def index_value_getter(a):
    print("List indices:")
    for i in range(len(a)):
        print(i)
    print()

    print("List values:")
    for i in range(len(a)):
        print(a[i])
    print()
    
    print("List indices/value:")
    for i in range(len(a)):
        print(i, a[i])

index_value_getter([7.0, 8.0, 10.0, 9.0, 10.0])
